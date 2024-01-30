import uuid

import chromadb
from chromadb.utils import embedding_functions
from datatypes import Document
from database import config


def get_new_uid():
    return uuid.uuid4().hex

def create_client():
    client = chromadb.PersistentClient(path=config.CHROMA_DATA_PATH)
    return client

def create_collection(client, collection_name=config.COLLECTION_NAME):
    embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction(
        model_name=config.EMBED_MODEL
    )
    collection = client.get_or_create_collection(
        name=collection_name,
        embedding_function=embedding_func,
        metadata={"hnsw:space": config.DISTANCE_METHOD},
    )
    return collection

def add_documents(collection, document:Document):
    document_id = get_new_uid()
    collection.add(documents=document.text,
                   metadatas={"name": document.name,
                              "summary": document.summary},
                   ids=document_id)
    return document_id

def search_documents(collection, query:str):
    query_results = collection.query(
        query_texts = [query],
        n_results = 2
    )
    return query_results


