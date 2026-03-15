from src.logger import logging
from src.exceptions import MyCustomeException
import os
import sys
from llama_index.core import VectorStoreIndex
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from google.genai.types import EmbedContentConfig
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from dotenv import load_dotenv


load_dotenv()

# def embedding_model(model_name = "gemini-embedding-001"):
#     try:
#         logging.info("loading the model")
#         embed_model = GoogleGenAIEmbedding(
#             model_name=model_name,
#             embed_batch_size=100,
#             output_dimensionality=786
#             )
#         return embed_model
#     except Exception as e:
#         logging.exception(e, exc_info=False)
#         raise MyCustomeException(e, sys)

def embedding_model(model_name: str = "sentence-transformers/all-MiniLM-L6-v2"):
    # token = os.getenv("HF_TOKEN")
    try:
        logging.info(f"loading the model: {model_name}")
        embed_model = HuggingFaceEmbedding(
            model_name=model_name,

            # model_kwargs={"token": token},
            # tokenizer_kwargs={"token": token}
        )
        return embed_model
    except Exception as e:
        logging.exception(e, exc_info=False)
        raise MyCustomeException(e, sys)
    

def transform_data(documents):
    try:
        logging.info("data transformation started...")

        for doc in documents:
            # 1. Sanitize and update the main text content
            clean_text = doc.get_content().encode("utf-8", "ignore").decode("utf-8")
            doc.set_content(clean_text)
            
            # 2. Sanitize string values in metadata (metadata IS usually a direct dict)
            for key, value in doc.metadata.items():
                if isinstance(value, str):
                    doc.metadata[key] = value.encode("utf-8", "ignore").decode("utf-8")
                    
        vector_index = VectorStoreIndex.from_documents(documents, embed_model=embedding_model(), show_progress=True)
        logging.info("data transformation finished...")
        return vector_index
    except Exception as e:
        logging.exception(e, exc_info=False)
        raise MyCustomeException(e, sys)