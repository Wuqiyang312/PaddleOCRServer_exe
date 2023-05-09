# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: data_feed.proto

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
  name='data_feed.proto',
  package='paddle.framework',
  syntax='proto2',
  serialized_pb=_b('\n\x0f\x64\x61ta_feed.proto\x12\x10paddle.framework\"b\n\x04Slot\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04type\x18\x02 \x02(\t\x12\x17\n\x08is_dense\x18\x03 \x01(\x08:\x05\x66\x61lse\x12\x16\n\x07is_used\x18\x04 \x01(\x08:\x05\x66\x61lse\x12\r\n\x05shape\x18\x05 \x03(\x05\"H\n\rMultiSlotDesc\x12%\n\x05slots\x18\x01 \x03(\x0b\x32\x16.paddle.framework.Slot\x12\x10\n\x08uid_slot\x18\x02 \x01(\t\"\x95\x02\n\x0bGraphConfig\x12\x16\n\x0bwalk_degree\x18\x01 \x01(\x05:\x01\x31\x12\x14\n\x08walk_len\x18\x02 \x01(\x05:\x02\x32\x30\x12\x11\n\x06window\x18\x03 \x01(\x05:\x01\x35\x12%\n\x17once_sample_startid_len\x18\x04 \x01(\x05:\x04\x38\x30\x30\x30\x12\"\n\x16sample_times_one_chunk\x18\x05 \x01(\x05:\x02\x31\x30\x12\x15\n\nbatch_size\x18\x06 \x01(\x05:\x01\x31\x12\x15\n\ndebug_mode\x18\x07 \x01(\x05:\x01\x30\x12\x17\n\x0f\x66irst_node_type\x18\x08 \x01(\t\x12\x11\n\tmeta_path\x18\t \x01(\t\x12 \n\x12gpu_graph_training\x18\n \x01(\x08:\x04true\"\xac\x02\n\x0c\x44\x61taFeedDesc\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x16\n\nbatch_size\x18\x02 \x01(\x05:\x02\x33\x32\x12\x38\n\x0fmulti_slot_desc\x18\x03 \x01(\x0b\x32\x1f.paddle.framework.MultiSlotDesc\x12\x14\n\x0cpipe_command\x18\x04 \x01(\t\x12\x12\n\nthread_num\x18\x05 \x01(\x05\x12\x13\n\x0brank_offset\x18\x06 \x01(\t\x12\x19\n\rpv_batch_size\x18\x07 \x01(\x05:\x02\x33\x32\x12\x15\n\ninput_type\x18\x08 \x01(\x05:\x01\x30\x12\x16\n\x0eso_parser_name\x18\t \x01(\t\x12\x33\n\x0cgraph_config\x18\n \x01(\x0b\x32\x1d.paddle.framework.GraphConfig')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_SLOT = _descriptor.Descriptor(
  name='Slot',
  full_name='paddle.framework.Slot',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='paddle.framework.Slot.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='paddle.framework.Slot.type', index=1,
      number=2, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_dense', full_name='paddle.framework.Slot.is_dense', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_used', full_name='paddle.framework.Slot.is_used', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='shape', full_name='paddle.framework.Slot.shape', index=4,
      number=5, type=5, cpp_type=1, label=3,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=37,
  serialized_end=135,
)


_MULTISLOTDESC = _descriptor.Descriptor(
  name='MultiSlotDesc',
  full_name='paddle.framework.MultiSlotDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='slots', full_name='paddle.framework.MultiSlotDesc.slots', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='uid_slot', full_name='paddle.framework.MultiSlotDesc.uid_slot', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=137,
  serialized_end=209,
)


_GRAPHCONFIG = _descriptor.Descriptor(
  name='GraphConfig',
  full_name='paddle.framework.GraphConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='walk_degree', full_name='paddle.framework.GraphConfig.walk_degree', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='walk_len', full_name='paddle.framework.GraphConfig.walk_len', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=20,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='window', full_name='paddle.framework.GraphConfig.window', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=5,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='once_sample_startid_len', full_name='paddle.framework.GraphConfig.once_sample_startid_len', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=8000,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sample_times_one_chunk', full_name='paddle.framework.GraphConfig.sample_times_one_chunk', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=10,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='paddle.framework.GraphConfig.batch_size', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='debug_mode', full_name='paddle.framework.GraphConfig.debug_mode', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='first_node_type', full_name='paddle.framework.GraphConfig.first_node_type', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='meta_path', full_name='paddle.framework.GraphConfig.meta_path', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gpu_graph_training', full_name='paddle.framework.GraphConfig.gpu_graph_training', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=True, default_value=True,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=212,
  serialized_end=489,
)


_DATAFEEDDESC = _descriptor.Descriptor(
  name='DataFeedDesc',
  full_name='paddle.framework.DataFeedDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='paddle.framework.DataFeedDesc.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='batch_size', full_name='paddle.framework.DataFeedDesc.batch_size', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='multi_slot_desc', full_name='paddle.framework.DataFeedDesc.multi_slot_desc', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pipe_command', full_name='paddle.framework.DataFeedDesc.pipe_command', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thread_num', full_name='paddle.framework.DataFeedDesc.thread_num', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank_offset', full_name='paddle.framework.DataFeedDesc.rank_offset', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pv_batch_size', full_name='paddle.framework.DataFeedDesc.pv_batch_size', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=32,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='input_type', full_name='paddle.framework.DataFeedDesc.input_type', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='so_parser_name', full_name='paddle.framework.DataFeedDesc.so_parser_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='graph_config', full_name='paddle.framework.DataFeedDesc.graph_config', index=9,
      number=10, type=11, cpp_type=10, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=492,
  serialized_end=792,
)

_MULTISLOTDESC.fields_by_name['slots'].message_type = _SLOT
_DATAFEEDDESC.fields_by_name['multi_slot_desc'].message_type = _MULTISLOTDESC
_DATAFEEDDESC.fields_by_name['graph_config'].message_type = _GRAPHCONFIG
DESCRIPTOR.message_types_by_name['Slot'] = _SLOT
DESCRIPTOR.message_types_by_name['MultiSlotDesc'] = _MULTISLOTDESC
DESCRIPTOR.message_types_by_name['GraphConfig'] = _GRAPHCONFIG
DESCRIPTOR.message_types_by_name['DataFeedDesc'] = _DATAFEEDDESC

Slot = _reflection.GeneratedProtocolMessageType('Slot', (_message.Message,), dict(
  DESCRIPTOR = _SLOT,
  __module__ = 'data_feed_pb2'
  # @@protoc_insertion_point(class_scope:paddle.framework.Slot)
  ))
_sym_db.RegisterMessage(Slot)

MultiSlotDesc = _reflection.GeneratedProtocolMessageType('MultiSlotDesc', (_message.Message,), dict(
  DESCRIPTOR = _MULTISLOTDESC,
  __module__ = 'data_feed_pb2'
  # @@protoc_insertion_point(class_scope:paddle.framework.MultiSlotDesc)
  ))
_sym_db.RegisterMessage(MultiSlotDesc)

GraphConfig = _reflection.GeneratedProtocolMessageType('GraphConfig', (_message.Message,), dict(
  DESCRIPTOR = _GRAPHCONFIG,
  __module__ = 'data_feed_pb2'
  # @@protoc_insertion_point(class_scope:paddle.framework.GraphConfig)
  ))
_sym_db.RegisterMessage(GraphConfig)

DataFeedDesc = _reflection.GeneratedProtocolMessageType('DataFeedDesc', (_message.Message,), dict(
  DESCRIPTOR = _DATAFEEDDESC,
  __module__ = 'data_feed_pb2'
  # @@protoc_insertion_point(class_scope:paddle.framework.DataFeedDesc)
  ))
_sym_db.RegisterMessage(DataFeedDesc)


# @@protoc_insertion_point(module_scope)
