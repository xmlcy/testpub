# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import mobile_base_mobility_pb2 as mobile__base__mobility__pb2
import part_pb2 as part__pb2


class MobileBaseMobilityServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendDirection = channel.unary_unary(
                '/reachy.part.mobile.base.mobility.MobileBaseMobilityService/SendDirection',
                request_serializer=mobile__base__mobility__pb2.TargetDirectionCommand.SerializeToString,
                response_deserializer=mobile__base__mobility__pb2.MobilityServiceAck.FromString,
                )
        self.SendSetSpeed = channel.unary_unary(
                '/reachy.part.mobile.base.mobility.MobileBaseMobilityService/SendSetSpeed',
                request_serializer=mobile__base__mobility__pb2.SetSpeedVector.SerializeToString,
                response_deserializer=mobile__base__mobility__pb2.MobilityServiceAck.FromString,
                )
        self.GetLastDirection = channel.unary_unary(
                '/reachy.part.mobile.base.mobility.MobileBaseMobilityService/GetLastDirection',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=mobile__base__mobility__pb2.DirectionVector.FromString,
                )
        self.DistanceToGoal = channel.unary_unary(
                '/reachy.part.mobile.base.mobility.MobileBaseMobilityService/DistanceToGoal',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=mobile__base__mobility__pb2.DistanceToGoalVector.FromString,
                )


class MobileBaseMobilityServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SendDirection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendSetSpeed(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetLastDirection(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DistanceToGoal(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MobileBaseMobilityServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendDirection': grpc.unary_unary_rpc_method_handler(
                    servicer.SendDirection,
                    request_deserializer=mobile__base__mobility__pb2.TargetDirectionCommand.FromString,
                    response_serializer=mobile__base__mobility__pb2.MobilityServiceAck.SerializeToString,
            ),
            'SendSetSpeed': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSetSpeed,
                    request_deserializer=mobile__base__mobility__pb2.SetSpeedVector.FromString,
                    response_serializer=mobile__base__mobility__pb2.MobilityServiceAck.SerializeToString,
            ),
            'GetLastDirection': grpc.unary_unary_rpc_method_handler(
                    servicer.GetLastDirection,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=mobile__base__mobility__pb2.DirectionVector.SerializeToString,
            ),
            'DistanceToGoal': grpc.unary_unary_rpc_method_handler(
                    servicer.DistanceToGoal,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=mobile__base__mobility__pb2.DistanceToGoalVector.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reachy.part.mobile.base.mobility.MobileBaseMobilityService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MobileBaseMobilityService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SendDirection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.mobility.MobileBaseMobilityService/SendDirection',
            mobile__base__mobility__pb2.TargetDirectionCommand.SerializeToString,
            mobile__base__mobility__pb2.MobilityServiceAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendSetSpeed(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.mobility.MobileBaseMobilityService/SendSetSpeed',
            mobile__base__mobility__pb2.SetSpeedVector.SerializeToString,
            mobile__base__mobility__pb2.MobilityServiceAck.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetLastDirection(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.mobility.MobileBaseMobilityService/GetLastDirection',
            part__pb2.PartId.SerializeToString,
            mobile__base__mobility__pb2.DirectionVector.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DistanceToGoal(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.mobile.base.mobility.MobileBaseMobilityService/DistanceToGoal',
            part__pb2.PartId.SerializeToString,
            mobile__base__mobility__pb2.DistanceToGoalVector.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
