﻿from set import PCCMeta

class join(object):
  def __init__(self, *classes):
    # List of classes that are part of join
    # should create a class when it gets called
    self.types = classes

  def __call__(self, actual_class):
    # actual_class the class that is being passed from application.
    class _Join(object):
      __metaclass__ = PCCMeta(actual_class)
      __dependent_type__ = True
      __ENTANGLED_TYPES__ = self.types
      __PCC_BASE_TYPE__ = False
      __pcc_bases__ = set([self.types])
      for tp in self.types:
         if hasattr(tp, "__pcc_bases__"):
            __pcc_bases__.update(tp.__pcc_bases__)

      __start_tracking__ = False
      
      
      def __init__(s, **kwargs):
        # kwargs just needs to have universe
        # unless it is parameterized, in which case it can have params also
        # Should not allow base class creation
        s._dataframe_universe = kwargs["universe"] if "universe" in kwargs else None
        s._nomerge = kwargs["nomerge"] if "nomerge" in kwargs else False
        
        # Collection of items that were generated by the query.
        # This is empty if "CreateSnapShot" is not invoked.
        s._items = []

      @staticmethod
      def Class():
        # Not sure if this should be exposed, 
        # as then people can create objects fromt this
        # useful for inheriting from class directly though.
        return actual_class

      @staticmethod
      def Create(*args, **kwargs):
        # The function that allows creation of the object.
        # If invariant is satisfied.
        if actual_class.__invariant__(*args, **kwargs):
          return actual_class(*args, **kwargs)
        else:
          raise TypeError("Invariant for " 
              + str(actual_class.__name__) 
              + "\n" 
              + "Not satisfied with arguments"
              + str(args) 
              + str(kwargs))

      @staticmethod
      def __invariant__(*args, **kwargs):
        return actual_class.__invariant__(*args, **kwargs)

      def All(s):
        return s._items

      def __enter__(s, *args):
        s.create_snapshot()
        return s

      def __exit__(s, *args):
        return s.merge() if not s._nomerge else None

      def _queryparams(s):
        return s._dataframe_universe.getcopies()

      def create_snapshot(s):
        s._items = actual_class.__query__(*s._queryparams())

      def merge(s):
        s._dataframe_universe.merge()
    
    return _Join