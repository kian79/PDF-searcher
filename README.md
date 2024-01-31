# Document Service

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## Overview

The Document Service is a Python project that provides a gRPC API for uploading, searching, and summarizing documents. It includes a gRPC server for handling document-related operations and can be easily deployed using Docker.

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






