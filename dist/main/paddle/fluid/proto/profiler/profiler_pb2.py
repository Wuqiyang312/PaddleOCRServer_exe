# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: profiler.proto

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
  name='profiler.proto',
  package='paddle.platform.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x0eprofiler.proto\x12\x15paddle.platform.proto\"\x18\n\x07MemCopy\x12\r\n\x05\x62ytes\x18\x01 \x01(\x04\"\x91\x02\n\x05\x45vent\x12\x34\n\x04type\x18\x08 \x01(\x0e\x32&.paddle.platform.proto.Event.EventType\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08start_ns\x18\x02 \x01(\x04\x12\x0e\n\x06\x65nd_ns\x18\x03 \x01(\x04\x12\x11\n\tdevice_id\x18\x05 \x01(\x03\x12\x15\n\rsub_device_id\x18\x06 \x01(\x03\x12/\n\x07memcopy\x18\x07 \x01(\x0b\x32\x1e.paddle.platform.proto.MemCopy\x12\x13\n\x0b\x64\x65tail_info\x18\t \x01(\t\"2\n\tEventType\x12\x07\n\x03\x43PU\x10\x00\x12\r\n\tGPUKernel\x10\x01\x12\r\n\tNPUKernel\x10\x02\"\x91\x02\n\x08MemEvent\x12\x10\n\x08start_ns\x18\x01 \x01(\x04\x12\x0e\n\x06\x65nd_ns\x18\x02 \x01(\x04\x12\r\n\x05\x62ytes\x18\x03 \x01(\x04\x12\x34\n\x05place\x18\x04 \x01(\x0e\x32%.paddle.platform.proto.MemEvent.Place\x12\x11\n\tthread_id\x18\x05 \x01(\x04\x12\x11\n\tdevice_id\x18\x06 \x01(\r\x12\x10\n\x08\x61lloc_in\x18\x07 \x01(\t\x12\x0f\n\x07\x66ree_in\x18\x08 \x01(\t\"U\n\x05Place\x12\r\n\tCUDAPlace\x10\x00\x12\x0c\n\x08\x43PUPlace\x10\x01\x12\x13\n\x0f\x43UDAPinnedPlace\x10\x02\x12\x0c\n\x08XPUPlace\x10\x03\x12\x0c\n\x08NPUPlace\x10\x04\"\x8e\x01\n\x07Profile\x12,\n\x06\x65vents\x18\x01 \x03(\x0b\x32\x1c.paddle.platform.proto.Event\x12\x10\n\x08start_ns\x18\x02 \x01(\x04\x12\x0e\n\x06\x65nd_ns\x18\x03 \x01(\x04\x12\x33\n\nmem_events\x18\x04 \x03(\x0b\x32\x1f.paddle.platform.proto.MemEvent')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_EVENT_EVENTTYPE = _descriptor.EnumDescriptor(
  name='EventType',
  full_name='paddle.platform.proto.Event.EventType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CPU', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GPUKernel', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NPUKernel', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=291,
  serialized_end=341,
)
_sym_db.RegisterEnumDescriptor(_EVENT_EVENTTYPE)

_MEMEVENT_PLACE = _descriptor.EnumDescriptor(
  name='Place',
  full_name='paddle.platform.proto.MemEvent.Place',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CUDAPlace', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CPUPlace', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CUDAPinnedPlace', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='XPUPlace', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NPUPlace', index=4, number=4,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=532,
  serialized_end=617,
)
_sym_db.RegisterEnumDescriptor(_MEMEVENT_PLACE)


_MEMCOPY = _descriptor.Descriptor(
  name='MemCopy',
  full_name='paddle.platform.proto.MemCopy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bytes', full_name='paddle.platform.proto.MemCopy.bytes', index=0,
      number=1, type=4, cpp_type=4, label=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=65,
)


_EVENT = _descriptor.Descriptor(
  name='Event',
  full_name='paddle.platform.proto.Event',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='paddle.platform.proto.Event.type', index=0,
      number=8, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='paddle.platform.proto.Event.name', index=1,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_ns', full_name='paddle.platform.proto.Event.start_ns', index=2,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_ns', full_name='paddle.platform.proto.Event.end_ns', index=3,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='paddle.platform.proto.Event.device_id', index=4,
      number=5, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sub_device_id', full_name='paddle.platform.proto.Event.sub_device_id', index=5,
      number=6, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='memcopy', full_name='paddle.platform.proto.Event.memcopy', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='detail_info', full_name='paddle.platform.proto.Event.detail_info', index=7,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _EVENT_EVENTTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=68,
  serialized_end=341,
)


_MEMEVENT = _descriptor.Descriptor(
  name='MemEvent',
  full_name='paddle.platform.proto.MemEvent',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start_ns', full_name='paddle.platform.proto.MemEvent.start_ns', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_ns', full_name='paddle.platform.proto.MemEvent.end_ns', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bytes', full_name='paddle.platform.proto.MemEvent.bytes', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='place', full_name='paddle.platform.proto.MemEvent.place', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='thread_id', full_name='paddle.platform.proto.MemEvent.thread_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='device_id', full_name='paddle.platform.proto.MemEvent.device_id', index=5,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='alloc_in', full_name='paddle.platform.proto.MemEvent.alloc_in', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='free_in', full_name='paddle.platform.proto.MemEvent.free_in', index=7,
      number=8, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _MEMEVENT_PLACE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=344,
  serialized_end=617,
)


_PROFILE = _descriptor.Descriptor(
  name='Profile',
  full_name='paddle.platform.proto.Profile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='events', full_name='paddle.platform.proto.Profile.events', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_ns', full_name='paddle.platform.proto.Profile.start_ns', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_ns', full_name='paddle.platform.proto.Profile.end_ns', index=2,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='mem_events', full_name='paddle.platform.proto.Profile.mem_events', index=3,
      number=4, type=11, cpp_type=10, label=3,
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
  serialized_start=620,
  serialized_end=762,
)

_EVENT.fields_by_name['type'].enum_type = _EVENT_EVENTTYPE
_EVENT.fields_by_name['memcopy'].message_type = _MEMCOPY
_EVENT_EVENTTYPE.containing_type = _EVENT
_MEMEVENT.fields_by_name['place'].enum_type = _MEMEVENT_PLACE
_MEMEVENT_PLACE.containing_type = _MEMEVENT
_PROFILE.fields_by_name['events'].message_type = _EVENT
_PROFILE.fields_by_name['mem_events'].message_type = _MEMEVENT
DESCRIPTOR.message_types_by_name['MemCopy'] = _MEMCOPY
DESCRIPTOR.message_types_by_name['Event'] = _EVENT
DESCRIPTOR.message_types_by_name['MemEvent'] = _MEMEVENT
DESCRIPTOR.message_types_by_name['Profile'] = _PROFILE

MemCopy = _reflection.GeneratedProtocolMessageType('MemCopy', (_message.Message,), dict(
  DESCRIPTOR = _MEMCOPY,
  __module__ = 'profiler_pb2'
  # @@protoc_insertion_point(class_scope:paddle.platform.proto.MemCopy)
  ))
_sym_db.RegisterMessage(MemCopy)

Event = _reflection.GeneratedProtocolMessageType('Event', (_message.Message,), dict(
  DESCRIPTOR = _EVENT,
  __module__ = 'profiler_pb2'
  # @@protoc_insertion_point(class_scope:paddle.platform.proto.Event)
  ))
_sym_db.RegisterMessage(Event)

MemEvent = _reflection.GeneratedProtocolMessageType('MemEvent', (_message.Message,), dict(
  DESCRIPTOR = _MEMEVENT,
  __module__ = 'profiler_pb2'
  # @@protoc_insertion_point(class_scope:paddle.platform.proto.MemEvent)
  ))
_sym_db.RegisterMessage(MemEvent)

Profile = _reflection.GeneratedProtocolMessageType('Profile', (_message.Message,), dict(
  DESCRIPTOR = _PROFILE,
  __module__ = 'profiler_pb2'
  # @@protoc_insertion_point(class_scope:paddle.platform.proto.Profile)
  ))
_sym_db.RegisterMessage(Profile)


# @@protoc_insertion_point(module_scope)
