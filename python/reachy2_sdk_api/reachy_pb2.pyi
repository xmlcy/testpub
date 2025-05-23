"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import arm_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import google.protobuf.timestamp_pb2
import hand_pb2
import head_pb2
import mobile_base_utility_pb2
import sys
import tripod_pb2
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _ReachyCoreMode:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _ReachyCoreModeEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_ReachyCoreMode.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    NONE: _ReachyCoreMode.ValueType  # 0
    FAKE: _ReachyCoreMode.ValueType  # 1
    REAL: _ReachyCoreMode.ValueType  # 2
    GAZEBO: _ReachyCoreMode.ValueType  # 3

class ReachyCoreMode(_ReachyCoreMode, metaclass=_ReachyCoreModeEnumTypeWrapper): ...

NONE: ReachyCoreMode.ValueType  # 0
FAKE: ReachyCoreMode.ValueType  # 1
REAL: ReachyCoreMode.ValueType  # 2
GAZEBO: ReachyCoreMode.ValueType  # 3
global___ReachyCoreMode = ReachyCoreMode

@typing_extensions.final
class Reachy(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    L_ARM_FIELD_NUMBER: builtins.int
    R_ARM_FIELD_NUMBER: builtins.int
    HEAD_FIELD_NUMBER: builtins.int
    L_HAND_FIELD_NUMBER: builtins.int
    R_HAND_FIELD_NUMBER: builtins.int
    MOBILE_BASE_FIELD_NUMBER: builtins.int
    TRIPOD_FIELD_NUMBER: builtins.int
    INFO_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> global___ReachyId: ...
    @property
    def l_arm(self) -> arm_pb2.Arm: ...
    @property
    def r_arm(self) -> arm_pb2.Arm: ...
    @property
    def head(self) -> head_pb2.Head: ...
    @property
    def l_hand(self) -> hand_pb2.Hand: ...
    @property
    def r_hand(self) -> hand_pb2.Hand: ...
    @property
    def mobile_base(self) -> mobile_base_utility_pb2.MobileBase: ...
    @property
    def tripod(self) -> tripod_pb2.Tripod: ...
    @property
    def info(self) -> global___ReachyInfo: ...
    def __init__(
        self,
        *,
        id: global___ReachyId | None = ...,
        l_arm: arm_pb2.Arm | None = ...,
        r_arm: arm_pb2.Arm | None = ...,
        head: head_pb2.Head | None = ...,
        l_hand: hand_pb2.Hand | None = ...,
        r_hand: hand_pb2.Hand | None = ...,
        mobile_base: mobile_base_utility_pb2.MobileBase | None = ...,
        tripod: tripod_pb2.Tripod | None = ...,
        info: global___ReachyInfo | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["head", b"head", "id", b"id", "info", b"info", "l_arm", b"l_arm", "l_hand", b"l_hand", "mobile_base", b"mobile_base", "r_arm", b"r_arm", "r_hand", b"r_hand", "tripod", b"tripod"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["head", b"head", "id", b"id", "info", b"info", "l_arm", b"l_arm", "l_hand", b"l_hand", "mobile_base", b"mobile_base", "r_arm", b"r_arm", "r_hand", b"r_hand", "tripod", b"tripod"]) -> None: ...

global___Reachy = Reachy

@typing_extensions.final
class ReachyId(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    id: builtins.int
    name: builtins.str
    def __init__(
        self,
        *,
        id: builtins.int = ...,
        name: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "name", b"name"]) -> None: ...

global___ReachyId = ReachyId

@typing_extensions.final
class ReachyInfo(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    SERIAL_NUMBER_FIELD_NUMBER: builtins.int
    VERSION_HARD_FIELD_NUMBER: builtins.int
    VERSION_SOFT_FIELD_NUMBER: builtins.int
    API_VERSION_FIELD_NUMBER: builtins.int
    CORE_MODE_FIELD_NUMBER: builtins.int
    serial_number: builtins.str
    version_hard: builtins.str
    version_soft: builtins.str
    api_version: builtins.str
    core_mode: global___ReachyCoreMode.ValueType
    def __init__(
        self,
        *,
        serial_number: builtins.str = ...,
        version_hard: builtins.str = ...,
        version_soft: builtins.str = ...,
        api_version: builtins.str = ...,
        core_mode: global___ReachyCoreMode.ValueType = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["api_version", b"api_version", "core_mode", b"core_mode", "serial_number", b"serial_number", "version_hard", b"version_hard", "version_soft", b"version_soft"]) -> None: ...

global___ReachyInfo = ReachyInfo

@typing_extensions.final
class ReachyState(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    L_ARM_STATE_FIELD_NUMBER: builtins.int
    R_ARM_STATE_FIELD_NUMBER: builtins.int
    HEAD_STATE_FIELD_NUMBER: builtins.int
    L_HAND_STATE_FIELD_NUMBER: builtins.int
    R_HAND_STATE_FIELD_NUMBER: builtins.int
    MOBILE_BASE_STATE_FIELD_NUMBER: builtins.int
    TRIPOD_STATE_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def id(self) -> global___ReachyId: ...
    @property
    def l_arm_state(self) -> arm_pb2.ArmState: ...
    @property
    def r_arm_state(self) -> arm_pb2.ArmState: ...
    @property
    def head_state(self) -> head_pb2.HeadState: ...
    @property
    def l_hand_state(self) -> hand_pb2.HandState: ...
    @property
    def r_hand_state(self) -> hand_pb2.HandState: ...
    @property
    def mobile_base_state(self) -> mobile_base_utility_pb2.MobileBaseState: ...
    @property
    def tripod_state(self) -> tripod_pb2.TripodState: ...
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        id: global___ReachyId | None = ...,
        l_arm_state: arm_pb2.ArmState | None = ...,
        r_arm_state: arm_pb2.ArmState | None = ...,
        head_state: head_pb2.HeadState | None = ...,
        l_hand_state: hand_pb2.HandState | None = ...,
        r_hand_state: hand_pb2.HandState | None = ...,
        mobile_base_state: mobile_base_utility_pb2.MobileBaseState | None = ...,
        tripod_state: tripod_pb2.TripodState | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["head_state", b"head_state", "id", b"id", "l_arm_state", b"l_arm_state", "l_hand_state", b"l_hand_state", "mobile_base_state", b"mobile_base_state", "r_arm_state", b"r_arm_state", "r_hand_state", b"r_hand_state", "timestamp", b"timestamp", "tripod_state", b"tripod_state"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["head_state", b"head_state", "id", b"id", "l_arm_state", b"l_arm_state", "l_hand_state", b"l_hand_state", "mobile_base_state", b"mobile_base_state", "r_arm_state", b"r_arm_state", "r_hand_state", b"r_hand_state", "timestamp", b"timestamp", "tripod_state", b"tripod_state"]) -> None: ...

global___ReachyState = ReachyState

@typing_extensions.final
class ReachyStatus(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    TIMESTAMP_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    L_ARM_STATUS_FIELD_NUMBER: builtins.int
    R_ARM_STATUS_FIELD_NUMBER: builtins.int
    HEAD_STATUS_FIELD_NUMBER: builtins.int
    L_HAND_STATUS_FIELD_NUMBER: builtins.int
    R_HAND_STATUS_FIELD_NUMBER: builtins.int
    MOBILE_BASE_STATUS_FIELD_NUMBER: builtins.int
    TRIPOD_STATUS_FIELD_NUMBER: builtins.int
    @property
    def timestamp(self) -> google.protobuf.timestamp_pb2.Timestamp: ...
    @property
    def id(self) -> global___ReachyId: ...
    @property
    def l_arm_status(self) -> arm_pb2.ArmStatus: ...
    @property
    def r_arm_status(self) -> arm_pb2.ArmStatus: ...
    @property
    def head_status(self) -> head_pb2.HeadStatus: ...
    @property
    def l_hand_status(self) -> hand_pb2.HandStatus: ...
    @property
    def r_hand_status(self) -> hand_pb2.HandStatus: ...
    @property
    def mobile_base_status(self) -> mobile_base_utility_pb2.MobileBaseStatus: ...
    @property
    def tripod_status(self) -> tripod_pb2.TripodStatus: ...
    def __init__(
        self,
        *,
        timestamp: google.protobuf.timestamp_pb2.Timestamp | None = ...,
        id: global___ReachyId | None = ...,
        l_arm_status: arm_pb2.ArmStatus | None = ...,
        r_arm_status: arm_pb2.ArmStatus | None = ...,
        head_status: head_pb2.HeadStatus | None = ...,
        l_hand_status: hand_pb2.HandStatus | None = ...,
        r_hand_status: hand_pb2.HandStatus | None = ...,
        mobile_base_status: mobile_base_utility_pb2.MobileBaseStatus | None = ...,
        tripod_status: tripod_pb2.TripodStatus | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["head_status", b"head_status", "id", b"id", "l_arm_status", b"l_arm_status", "l_hand_status", b"l_hand_status", "mobile_base_status", b"mobile_base_status", "r_arm_status", b"r_arm_status", "r_hand_status", b"r_hand_status", "timestamp", b"timestamp", "tripod_status", b"tripod_status"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["head_status", b"head_status", "id", b"id", "l_arm_status", b"l_arm_status", "l_hand_status", b"l_hand_status", "mobile_base_status", b"mobile_base_status", "r_arm_status", b"r_arm_status", "r_hand_status", b"r_hand_status", "timestamp", b"timestamp", "tripod_status", b"tripod_status"]) -> None: ...

global___ReachyStatus = ReachyStatus

@typing_extensions.final
class ReachyStreamStateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    PUBLISH_FREQUENCY_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> global___ReachyId: ...
    publish_frequency: builtins.float
    def __init__(
        self,
        *,
        id: global___ReachyId | None = ...,
        publish_frequency: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "publish_frequency", b"publish_frequency"]) -> None: ...

global___ReachyStreamStateRequest = ReachyStreamStateRequest

@typing_extensions.final
class ReachyStreamAuditRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    PUBLISH_FREQUENCY_FIELD_NUMBER: builtins.int
    @property
    def id(self) -> global___ReachyId: ...
    publish_frequency: builtins.float
    def __init__(
        self,
        *,
        id: global___ReachyId | None = ...,
        publish_frequency: builtins.float = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["id", b"id"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["id", b"id", "publish_frequency", b"publish_frequency"]) -> None: ...

global___ReachyStreamAuditRequest = ReachyStreamAuditRequest

@typing_extensions.final
class ReachyComponentsCommands(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    L_ARM_COMMANDS_FIELD_NUMBER: builtins.int
    R_ARM_COMMANDS_FIELD_NUMBER: builtins.int
    HEAD_COMMANDS_FIELD_NUMBER: builtins.int
    L_HAND_COMMANDS_FIELD_NUMBER: builtins.int
    R_HAND_COMMANDS_FIELD_NUMBER: builtins.int
    @property
    def l_arm_commands(self) -> arm_pb2.ArmComponentsCommands: ...
    @property
    def r_arm_commands(self) -> arm_pb2.ArmComponentsCommands: ...
    @property
    def head_commands(self) -> head_pb2.HeadComponentsCommands: ...
    @property
    def l_hand_commands(self) -> hand_pb2.HandPositionRequest: ...
    @property
    def r_hand_commands(self) -> hand_pb2.HandPositionRequest: ...
    def __init__(
        self,
        *,
        l_arm_commands: arm_pb2.ArmComponentsCommands | None = ...,
        r_arm_commands: arm_pb2.ArmComponentsCommands | None = ...,
        head_commands: head_pb2.HeadComponentsCommands | None = ...,
        l_hand_commands: hand_pb2.HandPositionRequest | None = ...,
        r_hand_commands: hand_pb2.HandPositionRequest | None = ...,
    ) -> None: ...
    def HasField(self, field_name: typing_extensions.Literal["head_commands", b"head_commands", "l_arm_commands", b"l_arm_commands", "l_hand_commands", b"l_hand_commands", "r_arm_commands", b"r_arm_commands", "r_hand_commands", b"r_hand_commands"]) -> builtins.bool: ...
    def ClearField(self, field_name: typing_extensions.Literal["head_commands", b"head_commands", "l_arm_commands", b"l_arm_commands", "l_hand_commands", b"l_hand_commands", "r_arm_commands", b"r_arm_commands", "r_hand_commands", b"r_hand_commands"]) -> None: ...

global___ReachyComponentsCommands = ReachyComponentsCommands
