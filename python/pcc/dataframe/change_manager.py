#################################################
#### Record keeping (Atomic Needed) #############
#################################################
from pcc.recursive_dictionary import RecursiveDictionary
from Queue import Queue
from queue_manager import QueueManager
from pcc.dataframe_changes.IDataframeChanges import Event
import pcc.dataframe_changes.IDataframeChanges as df_repr

class ChangeManager(object):
    def __init__(self):
        # Stores the object references for new, mod, and deleted.
        self.current_buffer = RecursiveDictionary()

        # groupname -> {oid -> proto object representing changes.}
        self.current_record = RecursiveDictionary()

        self.known_objects = RecursiveDictionary()

        self.deleted_objs = RecursiveDictionary()

        self.queue_manager = QueueManager()

        self.startrecording = False
        
    #################################################
    ### Static Methods ##############################
    #################################################
    
    #################################################
    ### API Methods #################################
    #################################################
    def report_dim_modification(self, records):
        for record in records:
            self.__record(record.event, record.tpname, record.groupname, record.oid, record.dim_change, record.full_obj, record.is_projection)

    def add_records(self, applied_records, pcc_change_records = None, except_app = None):
        records = (applied_records + pcc_change_records) if pcc_change_records else applied_records
        for rec in records:
            event, tpname, groupname, oid, dim_change, full_dim_map, is_projection  = (
                rec.event, rec.tpname, rec.groupname, rec.oid, rec.dim_change, rec.full_obj, rec.is_projection)
            self.__record(event, tpname, groupname, oid, dim_change, full_dim_map)
        self.__send_to_queues(applied_records, pcc_change_records, except_app)
        
    def add_changelog(self, changes):
        pass

    def get_record(self):
        return self.convert_to_serializable_dict(self.current_record)
    
    def add_app_queue(self, app_queue):
        return self.queue_manager.add_app_queue(app_queue)

    def build_change_map(self, records):
        the_dict = RecursiveDictionary()
        
    def convert_to_serializable_dict(self, current_record):
        df_changes = df_repr.DataframeChanges_Base()
        df_changes.ParseFromDict({"gc": current_record})
        return df_changes

    def clear_record(self):
        self.current_record = RecursiveDictionary()

    #################################################
    ### Private Methods #############################
    #################################################
    def __record_objs_to_dict(self, the_dict, tpname, groupname, oid, full_obj_map):
        objmap = the_dict.setdefault(groupname, RecursiveDictionary()).setdefault(oid, RecursiveDictionary())
        objmap.setdefault("types", RecursiveDictionary())[tpname] = Event.New
        objmap.setdefaykt("dims", RecursiveDictionary()).rec_update(full_obj_map)

    def __record(self, event_type, tpname, groupname, oid, dim_change, full_dim_map, is_projection = False):
        if not self.startrecording:
            return
        #for e event_type, tpname, oid, dim_changes in records:
        if event_type == Event.Delete and tpname == groupname:
            # it is its own key. Which means the obj is being deleted for good.
            # Purge all changes.
            if groupname in self.current_record and oid in self.current_record[groupname]:
                if "dims" in self.current_record[groupname][oid]:
                    del self.current_record[groupname][oid]["dims"]
                for tp in self.current_record[groupname][oid]["types"]:
                    self.current_record[groupname][oid]["types"][tp] = Event.Delete
            self.deleted_objs.setdefault(groupname, set()).add(oid)

                
        if event_type != Event.Delete and tpname in self.deleted_objs and oid in self.deleted_objs[tpname]:
            # This object is flagged for deletion. Throw this change away.
            return
        self.current_record.setdefault(
            groupname, RecursiveDictionary()).setdefault(
                oid, RecursiveDictionary({"types": RecursiveDictionary()}))["types"].rec_update(RecursiveDictionary({(groupname if event_type == Event.New and is_projection else tpname): event_type}))
        if dim_change:
            fks = []
            dims = self.current_record[groupname][oid].setdefault(
                        "dims", RecursiveDictionary())
            dims.rec_update(dim_change) 
            
    def __send_to_queues(self, applied_records, pcc_change_records, except_app = None):
        self.queue_manager.add_records(applied_records, pcc_change_records, except_app)
