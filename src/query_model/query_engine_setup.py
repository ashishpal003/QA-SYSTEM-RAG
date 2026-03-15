from src.logger import logging
from src.exceptions import MyCustomeException
import os
import sys
from llama_index.llms.google_genai import GoogleGenAI

def set_llm_model():
    try:
        logging.info("Intialize the model for RAG.")
        llm = GoogleGenAI(
            model="gemini-3.1-flash-lite-preview",
            temperature=0.8
        )
        return llm
    except Exception as e:
        logging.exception(e)
        raise MyCustomeException(e, sys)

def create_query_engine(index, llm):
    try:
        query_engine = index.as_query_engine(llm=llm)
        logging.info("Query Engine set for quering")
        return query_engine
    except Exception as e:
        logging.exception(e, exc_info=False)
        raise MyCustomeException(e, sys)