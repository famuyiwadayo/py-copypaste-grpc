# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: paste.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='paste.proto',
  package='paste',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x0bpaste.proto\x12\x05paste\"Z\n\x05Paste\x12\x0b\n\x03_id\x18\x01 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x02 \x01(\t\x12\x10\n\x08receiver\x18\x03 \x01(\t\x12\x0e\n\x06sender\x18\x04 \x01(\t\x12\x11\n\ttimestamp\x18\x05 \x01(\t\"=\n\x08PasteDTO\x12\x0f\n\x07\x63ontent\x18\x01 \x01(\t\x12\x10\n\x08receiver\x18\x02 \x01(\t\x12\x0e\n\x06sender\x18\x03 \x01(\t\"\x1e\n\nByReceiver\x12\x10\n\x08receiver\x18\x01 \x01(\t\"\x07\n\x05\x45MPTY2q\n\x0cPasteService\x12,\n\tSendPaste\x12\x0f.paste.PasteDTO\x1a\x0c.paste.EMPTY\"\x00\x12\x33\n\x0cReceivePaste\x12\x11.paste.ByReceiver\x1a\x0c.paste.Paste\"\x00\x30\x01\x62\x06proto3'
)




_PASTE = _descriptor.Descriptor(
  name='Paste',
  full_name='paste.Paste',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='_id', full_name='paste.Paste._id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='content', full_name='paste.Paste.content', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='paste.Paste.receiver', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='paste.Paste.sender', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='timestamp', full_name='paste.Paste.timestamp', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=22,
  serialized_end=112,
)


_PASTEDTO = _descriptor.Descriptor(
  name='PasteDTO',
  full_name='paste.PasteDTO',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='content', full_name='paste.PasteDTO.content', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='receiver', full_name='paste.PasteDTO.receiver', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='sender', full_name='paste.PasteDTO.sender', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=114,
  serialized_end=175,
)


_BYRECEIVER = _descriptor.Descriptor(
  name='ByReceiver',
  full_name='paste.ByReceiver',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='receiver', full_name='paste.ByReceiver.receiver', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=177,
  serialized_end=207,
)


_EMPTY = _descriptor.Descriptor(
  name='EMPTY',
  full_name='paste.EMPTY',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=209,
  serialized_end=216,
)

DESCRIPTOR.message_types_by_name['Paste'] = _PASTE
DESCRIPTOR.message_types_by_name['PasteDTO'] = _PASTEDTO
DESCRIPTOR.message_types_by_name['ByReceiver'] = _BYRECEIVER
DESCRIPTOR.message_types_by_name['EMPTY'] = _EMPTY
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Paste = _reflection.GeneratedProtocolMessageType('Paste', (_message.Message,), {
  'DESCRIPTOR' : _PASTE,
  '__module__' : 'paste_pb2'
  # @@protoc_insertion_point(class_scope:paste.Paste)
  })
_sym_db.RegisterMessage(Paste)

PasteDTO = _reflection.GeneratedProtocolMessageType('PasteDTO', (_message.Message,), {
  'DESCRIPTOR' : _PASTEDTO,
  '__module__' : 'paste_pb2'
  # @@protoc_insertion_point(class_scope:paste.PasteDTO)
  })
_sym_db.RegisterMessage(PasteDTO)

ByReceiver = _reflection.GeneratedProtocolMessageType('ByReceiver', (_message.Message,), {
  'DESCRIPTOR' : _BYRECEIVER,
  '__module__' : 'paste_pb2'
  # @@protoc_insertion_point(class_scope:paste.ByReceiver)
  })
_sym_db.RegisterMessage(ByReceiver)

EMPTY = _reflection.GeneratedProtocolMessageType('EMPTY', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'paste_pb2'
  # @@protoc_insertion_point(class_scope:paste.EMPTY)
  })
_sym_db.RegisterMessage(EMPTY)



_PASTESERVICE = _descriptor.ServiceDescriptor(
  name='PasteService',
  full_name='paste.PasteService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=218,
  serialized_end=331,
  methods=[
  _descriptor.MethodDescriptor(
    name='SendPaste',
    full_name='paste.PasteService.SendPaste',
    index=0,
    containing_service=None,
    input_type=_PASTEDTO,
    output_type=_EMPTY,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
  _descriptor.MethodDescriptor(
    name='ReceivePaste',
    full_name='paste.PasteService.ReceivePaste',
    index=1,
    containing_service=None,
    input_type=_BYRECEIVER,
    output_type=_PASTE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_PASTESERVICE)

DESCRIPTOR.services_by_name['PasteService'] = _PASTESERVICE

# @@protoc_insertion_point(module_scope)
