import sys
from src.logger import logging
from src.exceptions import MyCustomeException

from llama_index.core import SimpleDirectoryReader

def load_documents(data_path: str):
    """
    Load PDF documents from a specified directory.

    Parameters:
    - data (str): The path to the directory containing PDF files.

    Returns:
    - A list of loaded PDF documents. The specific type of documents may vary
    """
    try:
        logging.info("data loading started...")
        loader = SimpleDirectoryReader(input_files=[data_path])
        documents = loader.load_data(show_progress=True)
        logging.info("data loading completed...")
        return documents
    except Exception as e:
        logging.exception(e, exc_info=False)
        raise MyCustomeException(e, sys)
