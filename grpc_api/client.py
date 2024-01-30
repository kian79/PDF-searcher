import grpc
import document_service_pb2 as pb2
import document_service_pb2_grpc as pb2_grpc

def upload_document(file_content, document_name):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pb2_grpc.DocumentServiceStub(channel)
        request = pb2.UploadRequest(file_content=file_content, document_name=document_name)
        response = stub.UploadDocument(request)
        return response.document_id

def search_documents(query):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pb2_grpc.DocumentServiceStub(channel)
        request = pb2.SearchRequest(query=query)
        response = stub.SearchDocuments(request)
        return response.document_ids, response.document_summaries, response.document_texts

def summarize_text(text):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pb2_grpc.DocumentServiceStub(channel)
        request = pb2.SummarizeRequest(text=text)
        response = stub.SummarizeText(request)
        return response.summary
