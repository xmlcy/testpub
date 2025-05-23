"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import collections.abc
import error_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.wrappers_pb2
import part_pb2
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _HandType:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _HandTypeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_HandType.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NO_TYPE: _HandType.ValueType  # 0
    PARALLEL_GRIPPER: _HandType.ValueType  # 1

class HandType(_HandType, metaclass=_HandTypeEnumTypeWrapper): ...

NO_TYPE: HandType.ValueType  # 0
PARALLEL_GRIPPER: HandType.ValueType  # 1
global___HandType = HandType

class _SpeedLimit:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _SpeedLimitEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_SpeedLimit.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NO_LIMIT: _SpeedLimit.ValueType  # 0
    FAST: _SpeedLimit.ValueType  # 1
    NORMAL: _SpeedLimit.ValueType  # 2
    SLOW: _SpeedLimit.ValueType  # 3

class SpeedLimit(_SpeedLimit, metaclass=_SpeedLimitEnumTypeWrapper): ...

NO_LIMIT: SpeedLimit.ValueType  # 0
FAST: SpeedLimit.ValueType  # 1
NORMAL: SpeedLimit.ValueType  # 2
SLOW: SpeedLimit.ValueType  # 3
global___SpeedLimit = SpeedLimit

@typing_extensions.final
class Hand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PART_ID_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    @property
    def part_id(self) -> part_pb2.PartId: ...
    type: global___HandType.ValueType
    @property
    def info(self) -> part_pb2.PartInfo: ...
    def __init__(
        self,
        *,
        part_id: part_pb2.PartId | None = ...,
        type: global___HandType.ValueType = ...,
        info: part_pb2.PartInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["info", b"info", "part_id", b"part_id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["info", b"info", "part_id", b"part_id", "type", b"type"]) -> None: ...

global___Hand = Hand

@typing_extensions.final
class ListOfHand(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    HAND_FIELD_NUMBER: builtins.int
    @property
    def hand(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___Hand]: ...
    def __init__(
        self,
        *,
        hand: collections.abc.Iterable[global___Hand] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["hand", b"hand"]) -> None: ...

global___ListOfHand = ListOfHand

@typing_extensions.final
class HandState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPENING_FIELD_NUMBER: builtins.int
    FORCE_FIELD_NUMBER: builtins.int
    HOLDING_OBJECT_FIELD_NUMBER: builtins.int
    JOINTS_LIMITS_FIELD_NUMBER: builtins.int
    TEMPERATURES_FIELD_NUMBER: builtins.int
    PRESENT_POSITION_FIELD_NUMBER: builtins.int
    GOAL_POSITION_FIELD_NUMBER: builtins.int
    COMPLIANT_FIELD_NUMBER: builtins.int
    @property
    def opening(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def force(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def holding_object(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    @property
    def joints_limits(self) -> global___JointsLimits: ...
    @property
    def temperatures(self) -> global___HandTemperatures: ...
    @property
    def present_position(self) -> global___HandPosition: ...
    @property
    def goal_position(self) -> global___HandPosition: ...
    @property
    def compliant(self) -> google.protobuf.wrappers_pb2.BoolValue: ...
    def __init__(
        self,
        *,
        opening: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        force: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        holding_object: google.protobuf.wrappers_pb2.BoolValue | None = ...,
        joints_limits: global___JointsLimits | None = ...,
        temperatures: global___HandTemperatures | None = ...,
        present_position: global___HandPosition | None = ...,
        goal_position: global___HandPosition | None = ...,
        compliant: google.protobuf.wrappers_pb2.BoolValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "force", b"force", "goal_position", b"goal_position", "holding_object", b"holding_object", "joints_limits", b"joints_limits", "opening", b"opening", "present_position", b"present_position", "temperatures", b"temperatures"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["compliant", b"compliant", "force", b"force", "goal_position", b"goal_position", "holding_object", b"holding_object", "joints_limits", b"joints_limits", "opening", b"opening", "present_position", b"present_position", "temperatures", b"temperatures"]) -> None: ...

global___HandState = HandState

@typing_extensions.final
class HandStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ERRORS_FIELD_NUMBER: builtins.int
    @property
    def errors(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[error_pb2.Error]: ...
    def __init__(
        self,
        *,
        errors: collections.abc.Iterable[error_pb2.Error] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["errors", b"errors"]) -> None: ...

global___HandStatus = HandStatus

@typing_extensions.final
class Force(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    def __init__(
        self,
    ) -> None: ...

global___Force = Force

@typing_extensions.final
class JointLimits(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MIN_FIELD_NUMBER: builtins.int
    MAX_FIELD_NUMBER: builtins.int
    min: builtins.float
    max: builtins.float
    def __init__(
        self,
        *,
        min: builtins.float = ...,
        max: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["max", b"max", "min", b"min"]) -> None: ...

global___JointLimits = JointLimits

@typing_extensions.final
class ParallelGripperLimits(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    LIMITS_FIELD_NUMBER: builtins.int
    @property
    def limits(self) -> global___JointLimits: ...
    def __init__(
        self,
        *,
        limits: global___JointLimits | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["limits", b"limits"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["limits", b"limits"]) -> None: ...

global___ParallelGripperLimits = ParallelGripperLimits

@typing_extensions.final
class JointsLimits(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARALLEL_GRIPPER_FIELD_NUMBER: builtins.int
    @property
    def parallel_gripper(self) -> global___ParallelGripperLimits: ...
    def __init__(
        self,
        *,
        parallel_gripper: global___ParallelGripperLimits | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["limits", b"limits", "parallel_gripper", b"parallel_gripper"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["limits", b"limits", "parallel_gripper", b"parallel_gripper"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["limits", b"limits"]) -> typing_extensions.Literal["parallel_gripper"] | None: ...

global___JointsLimits = JointsLimits

@typing_extensions.final
class ParallelGripperPosition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    OPENING_PERCENTAGE_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    @property
    def opening_percentage(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    @property
    def position(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        opening_percentage: google.protobuf.wrappers_pb2.FloatValue | None = ...,
        position: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["gripper_position", b"gripper_position", "opening_percentage", b"opening_percentage", "position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["gripper_position", b"gripper_position", "opening_percentage", b"opening_percentage", "position", b"position"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["gripper_position", b"gripper_position"]) -> typing_extensions.Literal["opening_percentage", "position"] | None: ...

global___ParallelGripperPosition = ParallelGripperPosition

@typing_extensions.final
class HandPosition(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARALLEL_GRIPPER_FIELD_NUMBER: builtins.int
    @property
    def parallel_gripper(self) -> global___ParallelGripperPosition: ...
    def __init__(
        self,
        *,
        parallel_gripper: global___ParallelGripperPosition | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["parallel_gripper", b"parallel_gripper", "position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parallel_gripper", b"parallel_gripper", "position", b"position"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["position", b"position"]) -> typing_extensions.Literal["parallel_gripper"] | None: ...

global___HandPosition = HandPosition

@typing_extensions.final
class HandPositionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    POSITION_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    @property
    def position(self) -> global___HandPosition: ...
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        position: global___HandPosition | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id", "position", b"position"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "position", b"position"]) -> None: ...

global___HandPositionRequest = HandPositionRequest

@typing_extensions.final
class HandJointGoal(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    GOAL_REQUEST_FIELD_NUMBER: builtins.int
    DURATION_FIELD_NUMBER: builtins.int
    @property
    def goal_request(self) -> global___HandPositionRequest: ...
    @property
    def duration(self) -> google.protobuf.wrappers_pb2.FloatValue: ...
    def __init__(
        self,
        *,
        goal_request: global___HandPositionRequest | None = ...,
        duration: google.protobuf.wrappers_pb2.FloatValue | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["duration", b"duration", "goal_request", b"goal_request"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["duration", b"duration", "goal_request", b"goal_request"]) -> None: ...

global___HandJointGoal = HandJointGoal

@typing_extensions.final
class Temperatures(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    MOTOR_FIELD_NUMBER: builtins.int
    DRIVER_FIELD_NUMBER: builtins.int
    motor: builtins.float
    driver: builtins.float
    def __init__(
        self,
        *,
        motor: builtins.float = ...,
        driver: builtins.float = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["driver", b"driver", "motor", b"motor"]) -> None: ...

global___Temperatures = Temperatures

@typing_extensions.final
class ParallelGripperTemperature(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TEMPERATURE_FIELD_NUMBER: builtins.int
    @property
    def temperature(self) -> global___Temperatures: ...
    def __init__(
        self,
        *,
        temperature: global___Temperatures | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["temperature", b"temperature"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["temperature", b"temperature"]) -> None: ...

global___ParallelGripperTemperature = ParallelGripperTemperature

@typing_extensions.final
class HandTemperatures(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    PARALLEL_GRIPPER_FIELD_NUMBER: builtins.int
    @property
    def parallel_gripper(self) -> global___Temperatures: ...
    def __init__(
        self,
        *,
        parallel_gripper: global___Temperatures | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["parallel_gripper", b"parallel_gripper", "temperatures", b"temperatures"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["parallel_gripper", b"parallel_gripper", "temperatures", b"temperatures"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions.Literal["temperatures", b"temperatures"]) -> typing_extensions.Literal["parallel_gripper"] | None: ...

global___HandTemperatures = HandTemperatures

@typing_extensions.final
class SpeedLimitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    LIMIT_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> part_pb2.PartId: ...
    limit: global___SpeedLimit.ValueType
    def __init__(
        self,
        *,
        id: part_pb2.PartId | None = ...,
        limit: global___SpeedLimit.ValueType = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "limit", b"limit"]) -> None: ...

global___SpeedLimitRequest = SpeedLimitRequest
