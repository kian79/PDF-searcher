# PDF Searcher

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

The PDF Searcher is a Python project that provides a gRPC API for uploading, searching, and summarizing documents. It includes a gRPC server for handling document-related operations and can be easily deployed using Docker. It also uses [chromadb](https://docs.trychroma.com/) which is a vector database to store the data. After uploading the documents through the gRPC API the project converts the pdf file to text and embeds the text using [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2) which is a sentence-transformers model.

In addition to uploading documents and adding them to the database, you can call the APIs to search for a query in the database and summarizing your texts.

## Prerequisites

Make sure you have the following prerequisites installed:

- Python 3.8
- Docker
- Other dependencies (specified in `requirements.txt`)

## Getting Started

### Running Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/kian79/PDF-searcher.git
2. Navigate to the project directory:
   ```bash
   cd PDF_searcher
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
4. Run the gRPC server:
   ```bash
   pip install -r requirements.txt
5. Install dependencies:
   ```bash
   PYTHONPATH=.:.. python grpc_api/server.py
  The server should be running on localhost:50051.

### Docker Setup
1. Build the Docker image:
   ```bash
   docker build -t pdf_searcher .
2. Run the Docker container:
   ```bash
   docker run -p 50051:50051 pdf_searcher
  The gRPC server should be accessible on localhost:50051.

## Usage
To interact with the Document Service, you can use the provided gRPC client script or integrate the service into your own Python applications.

Example usage in Python client:

   ```bash
import grpc
import document_service_pb2 as pb2
import document_service_pb2_grpc as pb2_grpc

def upload_document(file_content, document_name):
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = pb2_grpc.DocumentServiceStub(channel)
        request = pb2.UploadRequest(file_content=file_content, document_name=document_name)
        response = stub.UploadDocument(request)
        return response.document_id

# Other client functions...

# Example usage:
with open("path/to/your/document.pdf", "rb") as file:
    pdf_content = file.read()

document_id = upload_document(pdf_content)
print(f"Uploaded document with ID: {document_id}")

