# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import mobile_base_mobility_pb2 as mobile__base__mobility__pb2
import mobile_base_utility_pb2 as mobile__base__utility__pb2
import part_pb2 as part__pb2


class MobileBaseUtilityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetAllMobileBases = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetAllMobileBases',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=mobile__base__utility__pb2.ListOfMobileBase.FromString,
                )
        self.GetState = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetState',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=mobile__base__utility__pb2.MobileBaseState.FromString,
                )
        self.Audit = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/Audit',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=mobile__base__utility__pb2.MobileBaseStatus.FromString,
                )
        self.HeartBeat = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/HeartBeat',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.Restart = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/Restart',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.TurnOn = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/TurnOn',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.TurnOff = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/TurnOff',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.SetControlMode = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/SetControlMode',
                request_serializer=mobile__base__utility__pb2.ControlModeCommand.SerializeToString,
                response_deserializer=mobile__base__mobility__pb2.MobilityServiceAck.FromString,
                )
        self.GetControlMode = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetControlMode',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=mobile__base__utility__pb2.ControlModeCommand.FromString,
                )
        self.SetZuuuMode = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/SetZuuuMode',
                request_serializer=mobile__base__utility__pb2.ZuuuModeCommand.SerializeToString,
                response_deserializer=mobile__base__mobility__pb2.MobilityServiceAck.FromString,
                )
        self.GetZuuuMode = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetZuuuMode',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=mobile__base__utility__pb2.ZuuuModeCommand.FromString,
                )
        self.GetBatteryLevel = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetBatteryLevel',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=mobile__base__utility__pb2.BatteryLevel.FromString,
                )
        self.GetOdometry = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetOdometry',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=mobile__base__utility__pb2.OdometryVector.FromString,
                )
        self.ResetOdometry = channel.unary_unary(
                '/reachy.part.mobile.base.utility.MobileBaseUtilityService/ResetOdometry',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=mobile__base__mobility__pb2.MobilityServiceAck.FromString,
                )


class MobileBaseUtilityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetAllMobileBases(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Audit(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def HeartBeat(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Restart(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TurnOn(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def TurnOff(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetControlMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetControlMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetZuuuMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetZuuuMode(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetBatteryLevel(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOdometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetOdometry(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MobileBaseUtilityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetAllMobileBases': grpc.unary_unary_rpc_method_handler(
                    servicer.GetAllMobileBases,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=mobile__base__utility__pb2.ListOfMobileBase.SerializeToString,
            ),
            'GetState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetState,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=mobile__base__utility__pb2.MobileBaseState.SerializeToString,
            ),
            'Audit': grpc.unary_unary_rpc_method_handler(
                    servicer.Audit,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=mobile__base__utility__pb2.MobileBaseStatus.SerializeToString,
            ),
            'HeartBeat': grpc.unary_unary_rpc_method_handler(
                    servicer.HeartBeat,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'Restart': grpc.unary_unary_rpc_method_handler(
                    servicer.Restart,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'TurnOn': grpc.unary_unary_rpc_method_handler(
                    servicer.TurnOn,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'TurnOff': grpc.unary_unary_rpc_method_handler(
                    servicer.TurnOff,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'SetControlMode': grpc.unary_unary_rpc_method_handler(
                    servicer.SetControlMode,
                    request_deserializer=mobile__base__utility__pb2.ControlModeCommand.FromString,
                    response_serializer=mobile__base__mobility__pb2.MobilityServiceAck.SerializeToString,
            ),
            'GetControlMode': grpc.unary_unary_rpc_method_handler(
                    servicer.GetControlMode,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=mobile__base__utility__pb2.ControlModeCommand.SerializeToString,
            ),
            'SetZuuuMode': grpc.unary_unary_rpc_method_handler(
                    servicer.SetZuuuMode,
                    request_deserializer=mobile__base__utility__pb2.ZuuuModeCommand.FromString,
                    response_serializer=mobile__base__mobility__pb2.MobilityServiceAck.SerializeToString,
            ),
            'GetZuuuMode': grpc.unary_unary_rpc_method_handler(
                    servicer.GetZuuuMode,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=mobile__base__utility__pb2.ZuuuModeCommand.SerializeToString,
            ),
            'GetBatteryLevel': grpc.unary_unary_rpc_method_handler(
                    servicer.GetBatteryLevel,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=mobile__base__utility__pb2.BatteryLevel.SerializeToString,
            ),
            'GetOdometry': grpc.unary_unary_rpc_method_handler(
                    servicer.GetOdometry,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=mobile__base__utility__pb2.OdometryVector.SerializeToString,
            ),
            'ResetOdometry': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetOdometry,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=mobile__base__mobility__pb2.MobilityServiceAck.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reachy.part.mobile.base.utility.MobileBaseUtilityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MobileBaseUtilityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetAllMobileBases(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetAllMobileBases',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            mobile__base__utility__pb2.ListOfMobileBase.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetState(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetState',
            part__pb2.PartId.SerializeToString,
            mobile__base__utility__pb2.MobileBaseState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Audit(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/Audit',
            part__pb2.PartId.SerializeToString,
            mobile__base__utility__pb2.MobileBaseStatus.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def HeartBeat(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/HeartBeat',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Restart(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/Restart',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TurnOn(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/TurnOn',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def TurnOff(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/TurnOff',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetControlMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/SetControlMode',
            mobile__base__utility__pb2.ControlModeCommand.SerializeToString,
            mobile__base__mobility__pb2.MobilityServiceAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetControlMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetControlMode',
            part__pb2.PartId.SerializeToString,
            mobile__base__utility__pb2.ControlModeCommand.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetZuuuMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/SetZuuuMode',
            mobile__base__utility__pb2.ZuuuModeCommand.SerializeToString,
            mobile__base__mobility__pb2.MobilityServiceAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetZuuuMode(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetZuuuMode',
            part__pb2.PartId.SerializeToString,
            mobile__base__utility__pb2.ZuuuModeCommand.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetBatteryLevel(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetBatteryLevel',
            part__pb2.PartId.SerializeToString,
            mobile__base__utility__pb2.BatteryLevel.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOdometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/GetOdometry',
            part__pb2.PartId.SerializeToString,
            mobile__base__utility__pb2.OdometryVector.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetOdometry(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.utility.MobileBaseUtilityService/ResetOdometry',
            part__pb2.PartId.SerializeToString,
            mobile__base__mobility__pb2.MobilityServiceAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
