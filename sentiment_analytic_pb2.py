# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: sentiment_analytic.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='sentiment_analytic.proto',
  package='SentimentAnalytic',
  syntax='proto3',
  serialized_options=b'\n\'io.grpc.sharkdetector.sentimentanalyticB\026SentimentAnalyticProtoP\001Z$github.com/chiupc/sentiment_analytic\242\002\003HLW',
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x18sentiment_analytic.proto\x12\x11SentimentAnalytic\"W\n\tInputFile\x12\x12\n\ncolumnName\x18\x01 \x01(\t\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\x12\x0c\n\x04text\x18\x03 \x01(\x0c\x12\x16\n\x0e\x61nalyzerEngine\x18\x04 \x01(\t\"3\n\nOutputFile\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x13\n\x0bsummaryData\x18\x02 \x01(\t2f\n\x11SentimentAnalytic\x12Q\n\x10\x41nalyzeSentiment\x12\x1c.SentimentAnalytic.InputFile\x1a\x1d.SentimentAnalytic.OutputFile\"\x00\x42o\n\'io.grpc.sharkdetector.sentimentanalyticB\x16SentimentAnalyticProtoP\x01Z$github.com/chiupc/sentiment_analytic\xa2\x02\x03HLWb\x06proto3'
)




_INPUTFILE = _descriptor.Descriptor(
  name='InputFile',
  full_name='SentimentAnalytic.InputFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='columnName', full_name='SentimentAnalytic.InputFile.columnName', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='fileName', full_name='SentimentAnalytic.InputFile.fileName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='SentimentAnalytic.InputFile.text', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=b"",
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='analyzerEngine', full_name='SentimentAnalytic.InputFile.analyzerEngine', index=3,
      number=4, type=9, cpp_type=9, label=1,
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
  serialized_start=47,
  serialized_end=134,
)


_OUTPUTFILE = _descriptor.Descriptor(
  name='OutputFile',
  full_name='SentimentAnalytic.OutputFile',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='filename', full_name='SentimentAnalytic.OutputFile.filename', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='summaryData', full_name='SentimentAnalytic.OutputFile.summaryData', index=1,
      number=2, type=9, cpp_type=9, label=1,
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
  serialized_start=136,
  serialized_end=187,
)

DESCRIPTOR.message_types_by_name['InputFile'] = _INPUTFILE
DESCRIPTOR.message_types_by_name['OutputFile'] = _OUTPUTFILE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputFile = _reflection.GeneratedProtocolMessageType('InputFile', (_message.Message,), {
  'DESCRIPTOR' : _INPUTFILE,
  '__module__' : 'sentiment_analytic_pb2'
  # @@protoc_insertion_point(class_scope:SentimentAnalytic.InputFile)
  })
_sym_db.RegisterMessage(InputFile)

OutputFile = _reflection.GeneratedProtocolMessageType('OutputFile', (_message.Message,), {
  'DESCRIPTOR' : _OUTPUTFILE,
  '__module__' : 'sentiment_analytic_pb2'
  # @@protoc_insertion_point(class_scope:SentimentAnalytic.OutputFile)
  })
_sym_db.RegisterMessage(OutputFile)


DESCRIPTOR._options = None

_SENTIMENTANALYTIC = _descriptor.ServiceDescriptor(
  name='SentimentAnalytic',
  full_name='SentimentAnalytic.SentimentAnalytic',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=189,
  serialized_end=291,
  methods=[
  _descriptor.MethodDescriptor(
    name='AnalyzeSentiment',
    full_name='SentimentAnalytic.SentimentAnalytic.AnalyzeSentiment',
    index=0,
    containing_service=None,
    input_type=_INPUTFILE,
    output_type=_OUTPUTFILE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_SENTIMENTANALYTIC)

DESCRIPTOR.services_by_name['SentimentAnalytic'] = _SENTIMENTANALYTIC

# @@protoc_insertion_point(module_scope)
