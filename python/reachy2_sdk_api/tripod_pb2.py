# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tripod.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
import component_pb2 as component__pb2
import error_pb2 as error__pb2
import part_pb2 as part__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0ctripod.proto\x12\x12reachy.part.tripod\x1a\x1bgoogle/protobuf/empty.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x0f\x63omponent.proto\x1a\x0b\x65rror.proto\x1a\npart.proto\"\x8f\x01\n\x06Tripod\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12:\n\x0b\x64\x65scription\x18\x02 \x01(\x0b\x32%.reachy.part.tripod.TripodDescription\x12#\n\x04info\x18\x05 \x01(\x0b\x32\x15.reachy.part.PartInfo\"J\n\x11TripodDescription\x12\x35\n\x0cheight_joint\x18\x01 \x01(\x0b\x32\x1f.reachy.part.tripod.TripodJoint\";\n\x0bTripodJoint\x12,\n\x04\x61xis\x18\x01 \x01(\x0e\x32\x1e.reachy.part.tripod.TripodAxis\"\xad\x01\n\x10TripodJointState\x12.\n\x05joint\x18\x01 \x01(\x0b\x32\x1f.reachy.part.tripod.TripodJoint\x12\x35\n\x10present_position\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\x12\x32\n\rgoal_position\x18\x03 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"i\n\x0bTripodState\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x34\n\x06height\x18\x02 \x01(\x0b\x32$.reachy.part.tripod.TripodJointState\"R\n\x0cTripodStatus\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x1c\n\x06\x65rrors\x18\x02 \x03(\x0b\x32\x0c.error.Error\"k\n\rTripodCommand\x12$\n\x07part_id\x18\x01 \x01(\x0b\x32\x13.reachy.part.PartId\x12\x34\n\x0fheight_position\x18\x02 \x01(\x0b\x32\x1b.google.protobuf.FloatValue\"B\n\x12TripodJointsLimits\x12,\n\x0cheight_limit\x18\x01 \x01(\x0b\x32\x16.component.JointLimits*\x18\n\nTripodAxis\x12\n\n\x06HEIGHT\x10\x00\x32\xef\x02\n\rTripodService\x12?\n\tGetTripod\x12\x16.google.protobuf.Empty\x1a\x1a.reachy.part.tripod.Tripod\x12@\n\x08GetState\x12\x13.reachy.part.PartId\x1a\x1f.reachy.part.tripod.TripodState\x12H\n\x0bSendCommand\x12!.reachy.part.tripod.TripodCommand\x1a\x16.google.protobuf.Empty\x12\x41\n\x12ResetDefaultValues\x12\x13.reachy.part.PartId\x1a\x16.google.protobuf.Empty\x12N\n\x0fGetJointsLimits\x12\x13.reachy.part.PartId\x1a&.reachy.part.tripod.TripodJointsLimitsb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'tripod_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_TRIPODAXIS']._serialized_start=966
  _globals['_TRIPODAXIS']._serialized_end=990
  _globals['_TRIPOD']._serialized_start=140
  _globals['_TRIPOD']._serialized_end=283
  _globals['_TRIPODDESCRIPTION']._serialized_start=285
  _globals['_TRIPODDESCRIPTION']._serialized_end=359
  _globals['_TRIPODJOINT']._serialized_start=361
  _globals['_TRIPODJOINT']._serialized_end=420
  _globals['_TRIPODJOINTSTATE']._serialized_start=423
  _globals['_TRIPODJOINTSTATE']._serialized_end=596
  _globals['_TRIPODSTATE']._serialized_start=598
  _globals['_TRIPODSTATE']._serialized_end=703
  _globals['_TRIPODSTATUS']._serialized_start=705
  _globals['_TRIPODSTATUS']._serialized_end=787
  _globals['_TRIPODCOMMAND']._serialized_start=789
  _globals['_TRIPODCOMMAND']._serialized_end=896
  _globals['_TRIPODJOINTSLIMITS']._serialized_start=898
  _globals['_TRIPODJOINTSLIMITS']._serialized_end=964
  _globals['_TRIPODSERVICE']._serialized_start=993
  _globals['_TRIPODSERVICE']._serialized_end=1360
# @@protoc_insertion_point(module_scope)
