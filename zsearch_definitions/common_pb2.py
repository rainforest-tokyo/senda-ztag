# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='zsearch',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x07zsearch\"\'\n\tMetadatum\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\xc1\x01\n\x0cUserdataAtom\x12\x15\n\rprivate_notes\x18\x01 \x01(\t\x12\x14\n\x0cpublic_notes\x18\x02 \x01(\t\x12,\n\x10private_metadata\x18\x03 \x03(\x0b\x32\x12.zsearch.Metadatum\x12+\n\x0fpublic_metadata\x18\x04 \x03(\x0b\x32\x12.zsearch.Metadatum\x12\x14\n\x0cprivate_tags\x18\x05 \x03(\t\x12\x13\n\x0bpublic_tags\x18\x06 \x03(\t\"\xb3\x01\n\x06\x41SAtom\x12\x0b\n\x03\x61sn\x18\x01 \x01(\r\x12\x13\n\x0b\x64\x65scription\x18\x02 \x01(\t\x12\x10\n\x04path\x18\x03 \x03(\rB\x02\x10\x01\x12\'\n\x03rir\x18\x04 \x01(\x0e\x32\x1a.zsearch.RegionalRegistrar\x12\x12\n\nbgp_prefix\x18\x05 \x01(\t\x12\x0c\n\x04name\x18\x06 \x01(\t\x12\x14\n\x0c\x63ountry_code\x18\x07 \x01(\t\x12\x14\n\x0corganization\x18\x08 \x01(\t*L\n\tDeltaType\x12\x0f\n\x0b\x44T_RESERVED\x10\x00\x12\r\n\tDT_UPDATE\x10\x01\x12\r\n\tDT_DELETE\x10\x02\x12\x10\n\x0c\x44T_NO_CHANGE\x10\x03*\x82\x01\n\x11RegionalRegistrar\x12\x10\n\x0cRIR_RESERVED\x10\x00\x12\x0c\n\x08RIR_ARIN\x10\x01\x12\x0c\n\x08RIR_RIPE\x10\x02\x12\r\n\tRIR_APNIC\x10\x03\x12\x0f\n\x0bRIR_AFRINIC\x10\x04\x12\x0e\n\nRIR_LACNIC\x10\x05\x12\x0f\n\x0bRIR_UNKNOWN\x10\x06\x62\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_DELTATYPE = _descriptor.EnumDescriptor(
  name='DeltaType',
  full_name='zsearch.DeltaType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DT_RESERVED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_UPDATE', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_DELETE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DT_NO_CHANGE', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=444,
  serialized_end=520,
)
_sym_db.RegisterEnumDescriptor(_DELTATYPE)

DeltaType = enum_type_wrapper.EnumTypeWrapper(_DELTATYPE)
_REGIONALREGISTRAR = _descriptor.EnumDescriptor(
  name='RegionalRegistrar',
  full_name='zsearch.RegionalRegistrar',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RIR_RESERVED', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIR_ARIN', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIR_RIPE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIR_APNIC', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIR_AFRINIC', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIR_LACNIC', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RIR_UNKNOWN', index=6, number=6,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=523,
  serialized_end=653,
)
_sym_db.RegisterEnumDescriptor(_REGIONALREGISTRAR)

RegionalRegistrar = enum_type_wrapper.EnumTypeWrapper(_REGIONALREGISTRAR)
DT_RESERVED = 0
DT_UPDATE = 1
DT_DELETE = 2
DT_NO_CHANGE = 3
RIR_RESERVED = 0
RIR_ARIN = 1
RIR_RIPE = 2
RIR_APNIC = 3
RIR_AFRINIC = 4
RIR_LACNIC = 5
RIR_UNKNOWN = 6



_METADATUM = _descriptor.Descriptor(
  name='Metadatum',
  full_name='zsearch.Metadatum',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='zsearch.Metadatum.key', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='value', full_name='zsearch.Metadatum.value', index=1,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=25,
  serialized_end=64,
)


_USERDATAATOM = _descriptor.Descriptor(
  name='UserdataAtom',
  full_name='zsearch.UserdataAtom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='private_notes', full_name='zsearch.UserdataAtom.private_notes', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_notes', full_name='zsearch.UserdataAtom.public_notes', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='private_metadata', full_name='zsearch.UserdataAtom.private_metadata', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_metadata', full_name='zsearch.UserdataAtom.public_metadata', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='private_tags', full_name='zsearch.UserdataAtom.private_tags', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='public_tags', full_name='zsearch.UserdataAtom.public_tags', index=5,
      number=6, type=9, cpp_type=9, label=3,
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
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=67,
  serialized_end=260,
)


_ASATOM = _descriptor.Descriptor(
  name='ASAtom',
  full_name='zsearch.ASAtom',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asn', full_name='zsearch.ASAtom.asn', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='description', full_name='zsearch.ASAtom.description', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='path', full_name='zsearch.ASAtom.path', index=2,
      number=3, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=_descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))),
    _descriptor.FieldDescriptor(
      name='rir', full_name='zsearch.ASAtom.rir', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='bgp_prefix', full_name='zsearch.ASAtom.bgp_prefix', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='zsearch.ASAtom.name', index=5,
      number=6, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='country_code', full_name='zsearch.ASAtom.country_code', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='organization', full_name='zsearch.ASAtom.organization', index=7,
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
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=263,
  serialized_end=442,
)

_USERDATAATOM.fields_by_name['private_metadata'].message_type = _METADATUM
_USERDATAATOM.fields_by_name['public_metadata'].message_type = _METADATUM
_ASATOM.fields_by_name['rir'].enum_type = _REGIONALREGISTRAR
DESCRIPTOR.message_types_by_name['Metadatum'] = _METADATUM
DESCRIPTOR.message_types_by_name['UserdataAtom'] = _USERDATAATOM
DESCRIPTOR.message_types_by_name['ASAtom'] = _ASATOM
DESCRIPTOR.enum_types_by_name['DeltaType'] = _DELTATYPE
DESCRIPTOR.enum_types_by_name['RegionalRegistrar'] = _REGIONALREGISTRAR

Metadatum = _reflection.GeneratedProtocolMessageType('Metadatum', (_message.Message,), dict(
  DESCRIPTOR = _METADATUM,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:zsearch.Metadatum)
  ))
_sym_db.RegisterMessage(Metadatum)

UserdataAtom = _reflection.GeneratedProtocolMessageType('UserdataAtom', (_message.Message,), dict(
  DESCRIPTOR = _USERDATAATOM,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:zsearch.UserdataAtom)
  ))
_sym_db.RegisterMessage(UserdataAtom)

ASAtom = _reflection.GeneratedProtocolMessageType('ASAtom', (_message.Message,), dict(
  DESCRIPTOR = _ASATOM,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:zsearch.ASAtom)
  ))
_sym_db.RegisterMessage(ASAtom)


_ASATOM.fields_by_name['path'].has_options = True
_ASATOM.fields_by_name['path']._options = _descriptor._ParseOptions(descriptor_pb2.FieldOptions(), _b('\020\001'))
# @@protoc_insertion_point(module_scope)
