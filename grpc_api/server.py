import grpc
from concurrent import futures
import document_service_pb2 as pb2
import document_service_pb2_grpc as pb2_grpc
from pdf_processing.preprocessing import convert_pdf_to_text, summarize_text
from database.chromadb import create_client, create_collection, add_documents, search_documents
from datatypes import Document
from grpc_api import config

class DocumentService(pb2_grpc.DocumentServiceServicer):
    def __init__(self, collection):
        self.collection = collection
    def UploadDocument(self, request, context):
        collection = self.collection
        pdf_content = request.file_content
        pdf_name = request.document_name
        pdf_temp_path = f'{pdf_name}.pdf'
        with open(pdf_temp_path, "wb") as pdf_file:
            pdf_file.write(pdf_content)
        pdf_text = convert_pdf_to_text(pdf_temp_path)
        pdf_summary = summarize_text(pdf_text)
        pdf_document = Document(text=pdf_text, summary=pdf_summary, name=pdf_name)
        document_id = add_documents(collection, document=pdf_document)
        return pb2.UploadResponse(document_id=document_id)

    def SearchDocuments(self, request, context):
        search_query = request.query
        query_results = search_documents(self.collection, search_query)
        result_ids = query_results["ids"][0]
        result_texts = query_results["documents"][0]
        result_summaries = query_results["metadatas"][0]
        # result_ids = ["1"]
        # result_texts = ["texts"]
        # result_summaries = ["texts"]
        print("result_ids: ", result_ids)
        print("result_texts: ", result_texts)
        print("result_summaries: ", result_summaries)
        return pb2.SearchResponse(document_ids=result_ids,
                                  document_summaries=result_summaries,
                                  document_texts=result_texts)

    def SummarizeText(self, request, context):
        text = request.text
        summary = summarize_text(text)
        return pb2.SummarizeResponse(summary=summary)

def serve():
    client = create_client()
    collection = create_collection(client)
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    pb2_grpc.add_DocumentServiceServicer_to_server(DocumentService(collection), server)
    server.add_insecure_port(f"{config.HOST}:{config.PORT}")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
    print('')
