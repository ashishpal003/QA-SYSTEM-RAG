from src.logger import logging
from src.exceptions import MyCustomeException
import os
import sys
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext, load_index_from_storage

def store_vectors(index: VectorStoreIndex) -> None:
    try:
        index.storage_context.persist(persist_dir="/Users/ashishpal/Documents/sunny_savita/QA-SYSTEM-RAG/vector_store")
        logging.info("Saved to local data store in the project root directory")
    except Exception as e:
        logging.exception(e, exc_info=False)
        raise MyCustomeException(e, sys)
    
def load_the_index(embed_model):
    try:
        storage_context = StorageContext.from_defaults(persist_dir="/Users/ashishpal/Documents/sunny_savita/QA-SYSTEM-RAG/vector_store")
        index = load_index_from_storage(storage_context, embed_model=embed_model )
        logging.info("local index store loaded")
        return index
    except Exception as e:
        logging.exception(e, exc_info=False)
        raise MyCustomeException(e, sys)
    








