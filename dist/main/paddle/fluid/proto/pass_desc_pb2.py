# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pass_desc.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import framework_pb2 as framework__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pass_desc.proto',
  package='paddle.framework.proto',
  syntax='proto2',
  serialized_pb=_b('\n\x0fpass_desc.proto\x12\x16paddle.framework.proto\x1a\x0f\x66ramework.proto\"\xd3\x0c\n\x08PassDesc\x12/\n\x07pattern\x18\x01 \x03(\x0b\x32\x1e.paddle.framework.proto.OpDesc\x12/\n\x07replace\x18\x02 \x03(\x0b\x32\x1e.paddle.framework.proto.OpDesc\x12\x39\n\x08var_maps\x18\x03 \x03(\x0b\x32\'.paddle.framework.proto.PassDesc.VarMap\x12?\n\rvar_attr_maps\x18\x04 \x03(\x0b\x32(.paddle.framework.proto.PassDesc.AttrMap\x12>\n\x0cop_attr_maps\x18\x05 \x03(\x0b\x32(.paddle.framework.proto.PassDesc.AttrMap\x12K\n\x13var_attr_conditions\x18\x06 \x03(\x0b\x32..paddle.framework.proto.PassDesc.AttrCondition\x12J\n\x12op_attr_conditions\x18\x07 \x03(\x0b\x32..paddle.framework.proto.PassDesc.AttrCondition\x1a\xe1\x01\n\x04\x41ttr\x12\x37\n\x04role\x18\x01 \x02(\x0e\x32).paddle.framework.proto.PassDesc.RoleType\x12\x10\n\x08var_name\x18\x02 \x01(\t\x12\x10\n\x08op_index\x18\x03 \x01(\x05\x12\x0c\n\x04name\x18\x04 \x02(\t\x12\x14\n\x0c\x65lement_name\x18\x05 \x01(\t\x12\x15\n\relement_index\x18\x06 \x01(\x05\x12\x41\n\toperation\x18\x07 \x01(\x0e\x32..paddle.framework.proto.PassDesc.OperationType\x1a\xb2\x01\n\tOperation\x12<\n\x04type\x18\x01 \x02(\x0e\x32..paddle.framework.proto.PassDesc.OperationType\x12\x33\n\x04\x61ttr\x18\x02 \x01(\x0b\x32%.paddle.framework.proto.PassDesc.Attr\x12\x32\n\x05value\x18\x03 \x01(\x0b\x32#.paddle.framework.proto.OpDesc.Attr\x1a\x32\n\x06VarMap\x12\x13\n\x0bpattern_var\x18\x01 \x02(\t\x12\x13\n\x0breplace_var\x18\x02 \x02(\t\x1a\xc2\x01\n\x07\x41ttrMap\x12;\n\x0cpattern_attr\x18\x01 \x02(\x0b\x32%.paddle.framework.proto.PassDesc.Attr\x12;\n\x0creplace_attr\x18\x02 \x02(\x0b\x32%.paddle.framework.proto.PassDesc.Attr\x12=\n\toperation\x18\x03 \x01(\x0b\x32*.paddle.framework.proto.PassDesc.Operation\x1a\xbe\x02\n\rAttrCondition\x12\x33\n\x04\x61ttr\x18\x01 \x02(\x0b\x32%.paddle.framework.proto.PassDesc.Attr\x12<\n\x04type\x18\x02 \x02(\x0e\x32..paddle.framework.proto.PassDesc.ConditionType\x12=\n\x0e\x63ondition_attr\x18\x03 \x01(\x0b\x32%.paddle.framework.proto.PassDesc.Attr\x12<\n\x0f\x63ondition_value\x18\x04 \x01(\x0b\x32#.paddle.framework.proto.OpDesc.Attr\x12=\n\toperation\x18\x05 \x01(\x0b\x32*.paddle.framework.proto.PassDesc.Operation\"(\n\x08RoleType\x12\r\n\tkVariable\x10\x00\x12\r\n\tkOperator\x10\x01\"L\n\rOperationType\x12\x08\n\x04kAdd\x10\x00\x12\x08\n\x04kSub\x10\x01\x12\x08\n\x04kMul\x10\x02\x12\x08\n\x04kDiv\x10\x03\x12\t\n\x05kSize\x10\x04\x12\x08\n\x04kMod\x10\x05\"E\n\rConditionType\x12\x07\n\x03kEQ\x10\x00\x12\x07\n\x03kNE\x10\x01\x12\x07\n\x03kGT\x10\x02\x12\x07\n\x03kGE\x10\x03\x12\x07\n\x03kLT\x10\x04\x12\x07\n\x03kLE\x10\x05\"X\n\rMultiPassDesc\x12\x11\n\tpass_type\x18\x01 \x01(\t\x12\x34\n\npass_descs\x18\x02 \x03(\x0b\x32 .paddle.framework.proto.PassDesc')
  ,
  dependencies=[framework__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_PASSDESC_ROLETYPE = _descriptor.EnumDescriptor(
  name='RoleType',
  full_name='paddle.framework.proto.PassDesc.RoleType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kVariable', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kOperator', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1491,
  serialized_end=1531,
)
_sym_db.RegisterEnumDescriptor(_PASSDESC_ROLETYPE)

_PASSDESC_OPERATIONTYPE = _descriptor.EnumDescriptor(
  name='OperationType',
  full_name='paddle.framework.proto.PassDesc.OperationType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kAdd', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSub', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kMul', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kDiv', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kSize', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kMod', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1533,
  serialized_end=1609,
)
_sym_db.RegisterEnumDescriptor(_PASSDESC_OPERATIONTYPE)

_PASSDESC_CONDITIONTYPE = _descriptor.EnumDescriptor(
  name='ConditionType',
  full_name='paddle.framework.proto.PassDesc.ConditionType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='kEQ', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kNE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kGT', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kGE', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kLT', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='kLE', index=5, number=5,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1611,
  serialized_end=1680,
)
_sym_db.RegisterEnumDescriptor(_PASSDESC_CONDITIONTYPE)


_PASSDESC_ATTR = _descriptor.Descriptor(
  name='Attr',
  full_name='paddle.framework.proto.PassDesc.Attr',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='role', full_name='paddle.framework.proto.PassDesc.Attr.role', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='var_name', full_name='paddle.framework.proto.PassDesc.Attr.var_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op_index', full_name='paddle.framework.proto.PassDesc.Attr.op_index', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='paddle.framework.proto.PassDesc.Attr.name', index=3,
      number=4, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='element_name', full_name='paddle.framework.proto.PassDesc.Attr.element_name', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='element_index', full_name='paddle.framework.proto.PassDesc.Attr.element_index', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='paddle.framework.proto.PassDesc.Attr.operation', index=6,
      number=7, type=14, cpp_type=8, label=1,
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
  serialized_start=513,
  serialized_end=738,
)

_PASSDESC_OPERATION = _descriptor.Descriptor(
  name='Operation',
  full_name='paddle.framework.proto.PassDesc.Operation',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='paddle.framework.proto.PassDesc.Operation.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='attr', full_name='paddle.framework.proto.PassDesc.Operation.attr', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='paddle.framework.proto.PassDesc.Operation.value', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=741,
  serialized_end=919,
)

_PASSDESC_VARMAP = _descriptor.Descriptor(
  name='VarMap',
  full_name='paddle.framework.proto.PassDesc.VarMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pattern_var', full_name='paddle.framework.proto.PassDesc.VarMap.pattern_var', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replace_var', full_name='paddle.framework.proto.PassDesc.VarMap.replace_var', index=1,
      number=2, type=9, cpp_type=9, label=2,
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
  serialized_start=921,
  serialized_end=971,
)

_PASSDESC_ATTRMAP = _descriptor.Descriptor(
  name='AttrMap',
  full_name='paddle.framework.proto.PassDesc.AttrMap',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pattern_attr', full_name='paddle.framework.proto.PassDesc.AttrMap.pattern_attr', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replace_attr', full_name='paddle.framework.proto.PassDesc.AttrMap.replace_attr', index=1,
      number=2, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='paddle.framework.proto.PassDesc.AttrMap.operation', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=974,
  serialized_end=1168,
)

_PASSDESC_ATTRCONDITION = _descriptor.Descriptor(
  name='AttrCondition',
  full_name='paddle.framework.proto.PassDesc.AttrCondition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='attr', full_name='paddle.framework.proto.PassDesc.AttrCondition.attr', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='paddle.framework.proto.PassDesc.AttrCondition.type', index=1,
      number=2, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_attr', full_name='paddle.framework.proto.PassDesc.AttrCondition.condition_attr', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='condition_value', full_name='paddle.framework.proto.PassDesc.AttrCondition.condition_value', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='operation', full_name='paddle.framework.proto.PassDesc.AttrCondition.operation', index=4,
      number=5, type=11, cpp_type=10, label=1,
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
  serialized_start=1171,
  serialized_end=1489,
)

_PASSDESC = _descriptor.Descriptor(
  name='PassDesc',
  full_name='paddle.framework.proto.PassDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pattern', full_name='paddle.framework.proto.PassDesc.pattern', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='replace', full_name='paddle.framework.proto.PassDesc.replace', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='var_maps', full_name='paddle.framework.proto.PassDesc.var_maps', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='var_attr_maps', full_name='paddle.framework.proto.PassDesc.var_attr_maps', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op_attr_maps', full_name='paddle.framework.proto.PassDesc.op_attr_maps', index=4,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='var_attr_conditions', full_name='paddle.framework.proto.PassDesc.var_attr_conditions', index=5,
      number=6, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='op_attr_conditions', full_name='paddle.framework.proto.PassDesc.op_attr_conditions', index=6,
      number=7, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_PASSDESC_ATTR, _PASSDESC_OPERATION, _PASSDESC_VARMAP, _PASSDESC_ATTRMAP, _PASSDESC_ATTRCONDITION, ],
  enum_types=[
    _PASSDESC_ROLETYPE,
    _PASSDESC_OPERATIONTYPE,
    _PASSDESC_CONDITIONTYPE,
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=61,
  serialized_end=1680,
)


_MULTIPASSDESC = _descriptor.Descriptor(
  name='MultiPassDesc',
  full_name='paddle.framework.proto.MultiPassDesc',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pass_type', full_name='paddle.framework.proto.MultiPassDesc.pass_type', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pass_descs', full_name='paddle.framework.proto.MultiPassDesc.pass_descs', index=1,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1682,
  serialized_end=1770,
)

_PASSDESC_ATTR.fields_by_name['role'].enum_type = _PASSDESC_ROLETYPE
_PASSDESC_ATTR.fields_by_name['operation'].enum_type = _PASSDESC_OPERATIONTYPE
_PASSDESC_ATTR.containing_type = _PASSDESC
_PASSDESC_OPERATION.fields_by_name['type'].enum_type = _PASSDESC_OPERATIONTYPE
_PASSDESC_OPERATION.fields_by_name['attr'].message_type = _PASSDESC_ATTR
_PASSDESC_OPERATION.fields_by_name['value'].message_type = framework__pb2._OPDESC_ATTR
_PASSDESC_OPERATION.containing_type = _PASSDESC
_PASSDESC_VARMAP.containing_type = _PASSDESC
_PASSDESC_ATTRMAP.fields_by_name['pattern_attr'].message_type = _PASSDESC_ATTR
_PASSDESC_ATTRMAP.fields_by_name['replace_attr'].message_type = _PASSDESC_ATTR
_PASSDESC_ATTRMAP.fields_by_name['operation'].message_type = _PASSDESC_OPERATION
_PASSDESC_ATTRMAP.containing_type = _PASSDESC
_PASSDESC_ATTRCONDITION.fields_by_name['attr'].message_type = _PASSDESC_ATTR
_PASSDESC_ATTRCONDITION.fields_by_name['type'].enum_type = _PASSDESC_CONDITIONTYPE
_PASSDESC_ATTRCONDITION.fields_by_name['condition_attr'].message_type = _PASSDESC_ATTR
_PASSDESC_ATTRCONDITION.fields_by_name['condition_value'].message_type = framework__pb2._OPDESC_ATTR
_PASSDESC_ATTRCONDITION.fields_by_name['operation'].message_type = _PASSDESC_OPERATION
_PASSDESC_ATTRCONDITION.containing_type = _PASSDESC
_PASSDESC.fields_by_name['pattern'].message_type = framework__pb2._OPDESC
_PASSDESC.fields_by_name['replace'].message_type = framework__pb2._OPDESC
_PASSDESC.fields_by_name['var_maps'].message_type = _PASSDESC_VARMAP
_PASSDESC.fields_by_name['var_attr_maps'].message_type = _PASSDESC_ATTRMAP
_PASSDESC.fields_by_name['op_attr_maps'].message_type = _PASSDESC_ATTRMAP
_PASSDESC.fields_by_name['var_attr_conditions'].message_type = _PASSDESC_ATTRCONDITION
_PASSDESC.fields_by_name['op_attr_conditions'].message_type = _PASSDESC_ATTRCONDITION
_PASSDESC_ROLETYPE.containing_type = _PASSDESC
_PASSDESC_OPERATIONTYPE.containing_type = _PASSDESC
_PASSDESC_CONDITIONTYPE.containing_type = _PASSDESC
_MULTIPASSDESC.fields_by_name['pass_descs'].message_type = _PASSDESC
DESCRIPTOR.message_types_by_name['PassDesc'] = _PASSDESC
DESCRIPTOR.message_types_by_name['MultiPassDesc'] = _MULTIPASSDESC

PassDesc = _reflection.GeneratedProtocolMessageType('PassDesc', (_message.Message,), dict(

  Attr = _reflection.GeneratedProtocolMessageType('Attr', (_message.Message,), dict(
    DESCRIPTOR = _PASSDESC_ATTR,
    __module__ = 'pass_desc_pb2'
    # @@protoc_insertion_point(class_scope:paddle.framework.proto.PassDesc.Attr)
    ))
  ,

  Operation = _reflection.GeneratedProtocolMessageType('Operation', (_message.Message,), dict(
    DESCRIPTOR = _PASSDESC_OPERATION,
    __module__ = 'pass_desc_pb2'
    # @@protoc_insertion_point(class_scope:paddle.framework.proto.PassDesc.Operation)
    ))
  ,

  VarMap = _reflection.GeneratedProtocolMessageType('VarMap', (_message.Message,), dict(
    DESCRIPTOR = _PASSDESC_VARMAP,
    __module__ = 'pass_desc_pb2'
    # @@protoc_insertion_point(class_scope:paddle.framework.proto.PassDesc.VarMap)
    ))
  ,

  AttrMap = _reflection.GeneratedProtocolMessageType('AttrMap', (_message.Message,), dict(
    DESCRIPTOR = _PASSDESC_ATTRMAP,
    __module__ = 'pass_desc_pb2'
    # @@protoc_insertion_point(class_scope:paddle.framework.proto.PassDesc.AttrMap)
    ))
  ,

  AttrCondition = _reflection.GeneratedProtocolMessageType('AttrCondition', (_message.Message,), dict(
    DESCRIPTOR = _PASSDESC_ATTRCONDITION,
    __module__ = 'pass_desc_pb2'
    # @@protoc_insertion_point(class_scope:paddle.framework.proto.PassDesc.AttrCondition)
    ))
  ,
  DESCRIPTOR = _PASSDESC,
  __module__ = 'pass_desc_pb2'
  # @@protoc_insertion_point(class_scope:paddle.framework.proto.PassDesc)
  ))
_sym_db.RegisterMessage(PassDesc)
_sym_db.RegisterMessage(PassDesc.Attr)
_sym_db.RegisterMessage(PassDesc.Operation)
_sym_db.RegisterMessage(PassDesc.VarMap)
_sym_db.RegisterMessage(PassDesc.AttrMap)
_sym_db.RegisterMessage(PassDesc.AttrCondition)

MultiPassDesc = _reflection.GeneratedProtocolMessageType('MultiPassDesc', (_message.Message,), dict(
  DESCRIPTOR = _MULTIPASSDESC,
  __module__ = 'pass_desc_pb2'
  # @@protoc_insertion_point(class_scope:paddle.framework.proto.MultiPassDesc)
  ))
_sym_db.RegisterMessage(MultiPassDesc)


# @@protoc_insertion_point(module_scope)
