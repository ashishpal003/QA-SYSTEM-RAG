## Here I am testing for logger setup
# from src.logger import logging

# print("Starting a test logging session....")
# print("Please check for a log folder.")
# logging.info('This is a test log.')

## Here I am testing for exception setup
# from src.exceptions import MyCustomeException
# import os
# import sys

# try:
#     a = 0
#     b = 10

#     c = b/a
# except Exception as e:
#     logging.exception(MyCustomeException(e, sys), exc_info=False)
#     raise MyCustomeException(e, sys)

## Here I am testing for data loading
from src.loading.data_ingestion import load_documents
from src.loading.data_transform import transform_data, embedding_model
from src.storing.vectore_store import store_vectors, load_the_index
from src.query_model.query_engine_setup import set_llm_model, create_query_engine

from llama_index.core import Settings

# document_path = "Complex-queries.pdf"
# document = load_documents(document_path)

# index = transform_data(document)

# store_vectors(index=index)

embed_model = embedding_model()
local_index = load_the_index(embed_model)

## set the model
llm = set_llm_model()
query_engine = create_query_engine(local_index, llm)

respose = query_engine.query("How to generate primary key values?")

print(respose)