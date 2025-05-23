# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import part_pb2 as part__pb2
import tripod_pb2 as tripod__pb2


class TripodServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetTripod = channel.unary_unary(
                '/reachy.part.tripod.TripodService/GetTripod',
                request_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
                response_deserializer=tripod__pb2.Tripod.FromString,
                )
        self.GetState = channel.unary_unary(
                '/reachy.part.tripod.TripodService/GetState',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=tripod__pb2.TripodState.FromString,
                )
        self.SendCommand = channel.unary_unary(
                '/reachy.part.tripod.TripodService/SendCommand',
                request_serializer=tripod__pb2.TripodCommand.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ResetDefaultValues = channel.unary_unary(
                '/reachy.part.tripod.TripodService/ResetDefaultValues',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.GetJointsLimits = channel.unary_unary(
                '/reachy.part.tripod.TripodService/GetJointsLimits',
                request_serializer=part__pb2.PartId.SerializeToString,
                response_deserializer=tripod__pb2.TripodJointsLimits.FromString,
                )


class TripodServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetTripod(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetState(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendCommand(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ResetDefaultValues(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetJointsLimits(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_TripodServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetTripod': grpc.unary_unary_rpc_method_handler(
                    servicer.GetTripod,
                    request_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                    response_serializer=tripod__pb2.Tripod.SerializeToString,
            ),
            'GetState': grpc.unary_unary_rpc_method_handler(
                    servicer.GetState,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=tripod__pb2.TripodState.SerializeToString,
            ),
            'SendCommand': grpc.unary_unary_rpc_method_handler(
                    servicer.SendCommand,
                    request_deserializer=tripod__pb2.TripodCommand.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ResetDefaultValues': grpc.unary_unary_rpc_method_handler(
                    servicer.ResetDefaultValues,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'GetJointsLimits': grpc.unary_unary_rpc_method_handler(
                    servicer.GetJointsLimits,
                    request_deserializer=part__pb2.PartId.FromString,
                    response_serializer=tripod__pb2.TripodJointsLimits.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'reachy.part.tripod.TripodService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class TripodService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetTripod(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.tripod.TripodService/GetTripod',
            google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            tripod__pb2.Tripod.FromString,
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
        return grpc.experimental.unary_unary(request, target, '/reachy.part.tripod.TripodService/GetState',
            part__pb2.PartId.SerializeToString,
            tripod__pb2.TripodState.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendCommand(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.tripod.TripodService/SendCommand',
            tripod__pb2.TripodCommand.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ResetDefaultValues(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.tripod.TripodService/ResetDefaultValues',
            part__pb2.PartId.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetJointsLimits(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/reachy.part.tripod.TripodService/GetJointsLimits',
            part__pb2.PartId.SerializeToString,
            tripod__pb2.TripodJointsLimits.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
