# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import document_service_pb2 as document__service__pb2


class DocumentServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.UploadDocument = channel.unary_unary(
                '/DocumentService/UploadDocument',
                request_serializer=document__service__pb2.UploadRequest.SerializeToString,
                response_deserializer=document__service__pb2.UploadResponse.FromString,
                )
        self.SearchDocuments = channel.unary_unary(
                '/DocumentService/SearchDocuments',
                request_serializer=document__service__pb2.SearchRequest.SerializeToString,
                response_deserializer=document__service__pb2.SearchResponse.FromString,
                )
        self.SummarizeText = channel.unary_unary(
                '/DocumentService/SummarizeText',
                request_serializer=document__service__pb2.SummarizeRequest.SerializeToString,
                response_deserializer=document__service__pb2.SummarizeResponse.FromString,
                )


class DocumentServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def UploadDocument(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchDocuments(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SummarizeText(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DocumentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'UploadDocument': grpc.unary_unary_rpc_method_handler(
                    servicer.UploadDocument,
                    request_deserializer=document__service__pb2.UploadRequest.FromString,
                    response_serializer=document__service__pb2.UploadResponse.SerializeToString,
            ),
            'SearchDocuments': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchDocuments,
                    request_deserializer=document__service__pb2.SearchRequest.FromString,
                    response_serializer=document__service__pb2.SearchResponse.SerializeToString,
            ),
            'SummarizeText': grpc.unary_unary_rpc_method_handler(
                    servicer.SummarizeText,
                    request_deserializer=document__service__pb2.SummarizeRequest.FromString,
                    response_serializer=document__service__pb2.SummarizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'DocumentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DocumentService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def UploadDocument(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DocumentService/UploadDocument',
            document__service__pb2.UploadRequest.SerializeToString,
            document__service__pb2.UploadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchDocuments(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DocumentService/SearchDocuments',
            document__service__pb2.SearchRequest.SerializeToString,
            document__service__pb2.SearchResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SummarizeText(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/DocumentService/SummarizeText',
            document__service__pb2.SummarizeRequest.SerializeToString,
            document__service__pb2.SummarizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
