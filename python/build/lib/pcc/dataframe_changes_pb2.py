# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dataframe_changes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='dataframe_changes.proto',
  package='Dataframe',
  serialized_pb=_b('\n\x17\x64\x61taframe_changes.proto\x12\tDataframe\"\xf5\x03\n\x05Value\x12\x11\n\tint_value\x18\x01 \x01(\x12\x12\x13\n\x0b\x66loat_value\x18\x02 \x01(\x01\x12\x11\n\tstr_value\x18\x03 \x01(\t\x12\x12\n\nbool_value\x18\x04 \x01(\x08\x12%\n\ncollection\x18\n \x03(\x0b\x32\x11.Dataframe.Record\x12\"\n\x03map\x18\x0b \x03(\x0b\x32\x15.Dataframe.Value.Pair\x12\'\n\x06object\x18\x0c \x01(\x0b\x32\x17.Dataframe.Value.Object\x12\x30\n\x0b\x66oreign_key\x18\r \x01(\x0b\x32\x1b.Dataframe.Value.ForeignKey\x1aH\n\x04Pair\x12\x1e\n\x03key\x18\x01 \x02(\x0b\x32\x11.Dataframe.Record\x12 \n\x05value\x18\x02 \x02(\x0b\x32\x11.Dataframe.Record\x1aR\n\x06Object\x12\x1d\n\x04type\x18\x01 \x01(\x0b\x32\x0f.Dataframe.Type\x12)\n\nobject_map\x18\x02 \x03(\x0b\x32\x15.Dataframe.Value.Pair\x1aY\n\nForeignKey\x12\x11\n\tgroup_key\x18\x01 \x02(\t\x12$\n\x0b\x61\x63tual_type\x18\x02 \x01(\x0b\x32\x0f.Dataframe.Type\x12\x12\n\nobject_key\x18\x03 \x02(\t\"\xdb\x01\n\x06Record\x12\x31\n\x0brecord_type\x18\x01 \x02(\x0e\x32\x1c.Dataframe.Record.RecordType\x12\x1f\n\x05value\x18\x02 \x01(\x0b\x32\x10.Dataframe.Value\"}\n\nRecordType\x12\x07\n\x03INT\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\n\n\x06STRING\x10\x03\x12\x08\n\x04\x42OOL\x10\x04\x12\x08\n\x04NULL\x10\x05\x12\x0e\n\nCOLLECTION\x10\n\x12\x0e\n\nDICTIONARY\x10\x0b\x12\n\n\x06OBJECT\x10\x0c\x12\x0f\n\x0b\x46OREIGN_KEY\x10\r\"L\n\x10\x44imensionChanges\x12\x16\n\x0e\x64imension_name\x18\x01 \x02(\t\x12 \n\x05value\x18\x02 \x01(\x0b\x32\x11.Dataframe.Record\"*\n\x04Type\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x14\n\x0ctype_pickled\x18\x02 \x01(\t\";\n\x05\x45vent\"2\n\tEventType\x12\n\n\x06\x44\x65lete\x10\x00\x12\x07\n\x03New\x10\x01\x12\x10\n\x0cModification\x10\x02\"W\n\x0bTypeChanges\x12\x1d\n\x04type\x18\x01 \x02(\x0b\x32\x0f.Dataframe.Type\x12)\n\x05\x65vent\x18\x02 \x02(\x0e\x32\x1a.Dataframe.Event.EventType\"\x89\x01\n\rObjectChanges\x12\x12\n\nobject_key\x18\x01 \x02(\t\x12\x36\n\x11\x64imension_changes\x18\x02 \x03(\x0b\x32\x1b.Dataframe.DimensionChanges\x12,\n\x0ctype_changes\x18\x03 \x03(\x0b\x32\x16.Dataframe.TypeChanges\"S\n\x0cGroupChanges\x12\x11\n\tgroup_key\x18\x01 \x02(\t\x12\x30\n\x0eobject_changes\x18\x02 \x03(\x0b\x32\x18.Dataframe.ObjectChanges\"b\n\x10\x44\x61taframeChanges\x12.\n\rgroup_changes\x18\x01 \x03(\x0b\x32\x17.Dataframe.GroupChanges\x12\x1e\n\x05types\x18\x02 \x03(\x0b\x32\x0f.Dataframe.Type')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_RECORD_RECORDTYPE = _descriptor.EnumDescriptor(
  name='RecordType',
  full_name='Dataframe.Record.RecordType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='INT', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FLOAT', index=1, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STRING', index=2, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOL', index=3, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NULL', index=4, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='COLLECTION', index=5, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DICTIONARY', index=6, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OBJECT', index=7, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FOREIGN_KEY', index=8, number=13,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=637,
  serialized_end=762,
)
_sym_db.RegisterEnumDescriptor(_RECORD_RECORDTYPE)

_EVENT_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='Dataframe.Event.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Delete', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='New', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Modification', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=895,
  serialized_end=945,
)
_sym_db.RegisterEnumDescriptor(_EVENT_EVENTTYPE)


_VALUE_PAIR = _descriptor.Descriptor(
  name='Pair',
  full_name='Dataframe.Value.Pair',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='Dataframe.Value.Pair.key', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dataframe.Value.Pair.value', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=293,
  serialized_end=365,
)

_VALUE_OBJECT = _descriptor.Descriptor(
  name='Object',
  full_name='Dataframe.Value.Object',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Dataframe.Value.Object.type', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_map', full_name='Dataframe.Value.Object.object_map', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=367,
  serialized_end=449,
)

_VALUE_FOREIGNKEY = _descriptor.Descriptor(
  name='ForeignKey',
  full_name='Dataframe.Value.ForeignKey',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_key', full_name='Dataframe.Value.ForeignKey.group_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='actual_type', full_name='Dataframe.Value.ForeignKey.actual_type', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_key', full_name='Dataframe.Value.ForeignKey.object_key', index=2,
      number=3, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=451,
  serialized_end=540,
)

_VALUE = _descriptor.Descriptor(
  name='Value',
  full_name='Dataframe.Value',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='int_value', full_name='Dataframe.Value.int_value', index=0,
      number=1, type=18, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='float_value', full_name='Dataframe.Value.float_value', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='str_value', full_name='Dataframe.Value.str_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bool_value', full_name='Dataframe.Value.bool_value', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='collection', full_name='Dataframe.Value.collection', index=4,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='map', full_name='Dataframe.Value.map', index=5,
      number=11, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object', full_name='Dataframe.Value.object', index=6,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='foreign_key', full_name='Dataframe.Value.foreign_key', index=7,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_VALUE_PAIR, _VALUE_OBJECT, _VALUE_FOREIGNKEY, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=39,
  serialized_end=540,
)


_RECORD = _descriptor.Descriptor(
  name='Record',
  full_name='Dataframe.Record',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='record_type', full_name='Dataframe.Record.record_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dataframe.Record.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _RECORD_RECORDTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=543,
  serialized_end=762,
)


_DIMENSIONCHANGES = _descriptor.Descriptor(
  name='DimensionChanges',
  full_name='Dataframe.DimensionChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='dimension_name', full_name='Dataframe.DimensionChanges.dimension_name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='Dataframe.DimensionChanges.value', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=764,
  serialized_end=840,
)


_TYPE = _descriptor.Descriptor(
  name='Type',
  full_name='Dataframe.Type',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='Dataframe.Type.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_pickled', full_name='Dataframe.Type.type_pickled', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=842,
  serialized_end=884,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='Dataframe.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENT_EVENTTYPE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=886,
  serialized_end=945,
)


_TYPECHANGES = _descriptor.Descriptor(
  name='TypeChanges',
  full_name='Dataframe.TypeChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Dataframe.TypeChanges.type', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='event', full_name='Dataframe.TypeChanges.event', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=947,
  serialized_end=1034,
)


_OBJECTCHANGES = _descriptor.Descriptor(
  name='ObjectChanges',
  full_name='Dataframe.ObjectChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='object_key', full_name='Dataframe.ObjectChanges.object_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='dimension_changes', full_name='Dataframe.ObjectChanges.dimension_changes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type_changes', full_name='Dataframe.ObjectChanges.type_changes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1037,
  serialized_end=1174,
)


_GROUPCHANGES = _descriptor.Descriptor(
  name='GroupChanges',
  full_name='Dataframe.GroupChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_key', full_name='Dataframe.GroupChanges.group_key', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='object_changes', full_name='Dataframe.GroupChanges.object_changes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1176,
  serialized_end=1259,
)


_DATAFRAMECHANGES = _descriptor.Descriptor(
  name='DataframeChanges',
  full_name='Dataframe.DataframeChanges',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='group_changes', full_name='Dataframe.DataframeChanges.group_changes', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='types', full_name='Dataframe.DataframeChanges.types', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1261,
  serialized_end=1359,
)

_VALUE_PAIR.fields_by_name['key'].message_type = _RECORD
_VALUE_PAIR.fields_by_name['value'].message_type = _RECORD
_VALUE_PAIR.containing_type = _VALUE
_VALUE_OBJECT.fields_by_name['type'].message_type = _TYPE
_VALUE_OBJECT.fields_by_name['object_map'].message_type = _VALUE_PAIR
_VALUE_OBJECT.containing_type = _VALUE
_VALUE_FOREIGNKEY.fields_by_name['actual_type'].message_type = _TYPE
_VALUE_FOREIGNKEY.containing_type = _VALUE
_VALUE.fields_by_name['collection'].message_type = _RECORD
_VALUE.fields_by_name['map'].message_type = _VALUE_PAIR
_VALUE.fields_by_name['object'].message_type = _VALUE_OBJECT
_VALUE.fields_by_name['foreign_key'].message_type = _VALUE_FOREIGNKEY
_RECORD.fields_by_name['record_type'].enum_type = _RECORD_RECORDTYPE
_RECORD.fields_by_name['value'].message_type = _VALUE
_RECORD_RECORDTYPE.containing_type = _RECORD
_DIMENSIONCHANGES.fields_by_name['value'].message_type = _RECORD
_EVENT_EVENTTYPE.containing_type = _EVENT
_TYPECHANGES.fields_by_name['type'].message_type = _TYPE
_TYPECHANGES.fields_by_name['event'].enum_type = _EVENT_EVENTTYPE
_OBJECTCHANGES.fields_by_name['dimension_changes'].message_type = _DIMENSIONCHANGES
_OBJECTCHANGES.fields_by_name['type_changes'].message_type = _TYPECHANGES
_GROUPCHANGES.fields_by_name['object_changes'].message_type = _OBJECTCHANGES
_DATAFRAMECHANGES.fields_by_name['group_changes'].message_type = _GROUPCHANGES
_DATAFRAMECHANGES.fields_by_name['types'].message_type = _TYPE
DESCRIPTOR.message_types_by_name['Value'] = _VALUE
DESCRIPTOR.message_types_by_name['Record'] = _RECORD
DESCRIPTOR.message_types_by_name['DimensionChanges'] = _DIMENSIONCHANGES
DESCRIPTOR.message_types_by_name['Type'] = _TYPE
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['TypeChanges'] = _TYPECHANGES
DESCRIPTOR.message_types_by_name['ObjectChanges'] = _OBJECTCHANGES
DESCRIPTOR.message_types_by_name['GroupChanges'] = _GROUPCHANGES
DESCRIPTOR.message_types_by_name['DataframeChanges'] = _DATAFRAMECHANGES

Value = _reflection.GeneratedProtocolMessageType('Value', (_message.Message,), dict(

  Pair = _reflection.GeneratedProtocolMessageType('Pair', (_message.Message,), dict(
    DESCRIPTOR = _VALUE_PAIR,
    __module__ = 'dataframe_changes_pb2'
    # @@protoc_insertion_point(class_scope:Dataframe.Value.Pair)
    ))
  ,

  Object = _reflection.GeneratedProtocolMessageType('Object', (_message.Message,), dict(
    DESCRIPTOR = _VALUE_OBJECT,
    __module__ = 'dataframe_changes_pb2'
    # @@protoc_insertion_point(class_scope:Dataframe.Value.Object)
    ))
  ,

  ForeignKey = _reflection.GeneratedProtocolMessageType('ForeignKey', (_message.Message,), dict(
    DESCRIPTOR = _VALUE_FOREIGNKEY,
    __module__ = 'dataframe_changes_pb2'
    # @@protoc_insertion_point(class_scope:Dataframe.Value.ForeignKey)
    ))
  ,
  DESCRIPTOR = _VALUE,
  __module__ = 'dataframe_changes_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe.Value)
  ))
_sym_db.RegisterMessage(Value)
_sym_db.RegisterMessage(Value.Pair)
_sym_db.RegisterMessage(Value.Object)
_sym_db.RegisterMessage(Value.ForeignKey)

Record = _reflection.GeneratedProtocolMessageType('Record', (_message.Message,), dict(
  DESCRIPTOR = _RECORD,
  __module__ = 'dataframe_changes_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe.Record)
  ))
_sym_db.RegisterMessage(Record)

DimensionChanges = _reflection.GeneratedProtocolMessageType('DimensionChanges', (_message.Message,), dict(
  DESCRIPTOR = _DIMENSIONCHANGES,
  __module__ = 'dataframe_changes_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe.DimensionChanges)
  ))
_sym_db.RegisterMessage(DimensionChanges)

Type = _reflection.GeneratedProtocolMessageType('Type', (_message.Message,), dict(
  DESCRIPTOR = _TYPE,
  __module__ = 'dataframe_changes_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe.Type)
  ))
_sym_db.RegisterMessage(Type)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'dataframe_changes_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe.Event)
  ))
_sym_db.RegisterMessage(Event)

TypeChanges = _reflection.GeneratedProtocolMessageType('TypeChanges', (_message.Message,), dict(
  DESCRIPTOR = _TYPECHANGES,
  __module__ = 'dataframe_changes_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe.TypeChanges)
  ))
_sym_db.RegisterMessage(TypeChanges)

ObjectChanges = _reflection.GeneratedProtocolMessageType('ObjectChanges', (_message.Message,), dict(
  DESCRIPTOR = _OBJECTCHANGES,
  __module__ = 'dataframe_changes_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe.ObjectChanges)
  ))
_sym_db.RegisterMessage(ObjectChanges)

GroupChanges = _reflection.GeneratedProtocolMessageType('GroupChanges', (_message.Message,), dict(
  DESCRIPTOR = _GROUPCHANGES,
  __module__ = 'dataframe_changes_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe.GroupChanges)
  ))
_sym_db.RegisterMessage(GroupChanges)

DataframeChanges = _reflection.GeneratedProtocolMessageType('DataframeChanges', (_message.Message,), dict(
  DESCRIPTOR = _DATAFRAMECHANGES,
  __module__ = 'dataframe_changes_pb2'
  # @@protoc_insertion_point(class_scope:Dataframe.DataframeChanges)
  ))
_sym_db.RegisterMessage(DataframeChanges)


# @@protoc_insertion_point(module_scope)