# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: GMT.proto
# Protobuf Python Version: 4.25.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\tGMT.proto\"$\n\x10TimeStampRequest\x12\x10\n\x08\x64ocument\x18\x01 \x01(\x0c\"9\n\x11TimeStampResponse\x12\x11\n\tsignature\x18\x01 \x01(\t\x12\x11\n\ttimestamp\x18\x02 \x01(\t2S\n\x10TimeStampService\x12?\n\x14GetDocumentTimeStamp\x12\x11.TimeStampRequest\x1a\x12.TimeStampResponse\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GMT_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TIMESTAMPREQUEST']._serialized_start=13
  _globals['_TIMESTAMPREQUEST']._serialized_end=49
  _globals['_TIMESTAMPRESPONSE']._serialized_start=51
  _globals['_TIMESTAMPRESPONSE']._serialized_end=108
  _globals['_TIMESTAMPSERVICE']._serialized_start=110
  _globals['_TIMESTAMPSERVICE']._serialized_end=193
# @@protoc_insertion_point(module_scope)
