This project implements a Retrieval-Augmented Generation (RAG) pipeline. It queries local documents using LlamaIndex, Hugging Face embeddings, and Google Gemini.

## Getting Started

### Project Initialization

# QA System for local documents with LlamaIndex, HuggingFace and Google Gemini
This project uses a Retrieval-Augmented Generation (RAG) pipeline to query local documents. It uses LlamaIndex, HuggingFace embeddings, and Google Gemini.

## 🚀 Project Template
Run the template script to create the project structure:

```bash
python template.py

Note: Add a requirements.txt file and a .env file to the folder.
🛠️ Build the Project

   1. Set up setup.py.
   2. Add -e . to your requirements.txt file.
   3. Run the following command:

pip install -r requirements.txt

This builds the project so custom modules can be called by other modules as soon as they are created.

## 📝 Logging and Custom Exceptions
The project includes modules to track the pipeline and identify code issues:

* src/logger/__init__.py
* src/exception/__init__.py

## 📥 Data Ingestion Pipeline
This pipeline starts with local data on the system. Documents are chunked and embedded using LlamaIndex: [3] 

* Tool: SimpleDirectoryReader(input_dir=data_path)

## ⚙️ Data Transformation Pipeline
This stage uses the SimpleDirectoryReader object from the ingestion pipeline:

* Cleaning: Text in the nodes is cleaned of encoding issues.
* Embeddings: Text is converted to embeddings using a HuggingFace model. [4] 

## 💾 Storing
Embeddings are stored in a local directory.
Note: While this project uses a simple local store, local vector DBs such as Chroma or FAISS can be applied to increase retrieval speed.

## 🔍 Query Model
This section uses the LLM (Google Gemini) to generate answers based on user queries and retrieved embeddings. The Query Engine orchestrates:

   1. Query Embedding: Generated using the same HuggingFace model.
   2. Retrieval: Relevant embeddings and text are retrieved via similarity search.
   3. Response: The LLM generates the final answer using the retrieved context.

## 💻 Streamlit App
A Streamlit user interface is provided for interaction with the system.

