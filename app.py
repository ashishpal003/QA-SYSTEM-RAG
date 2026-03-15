import streamlit as st
import llama_index
from src.loading.data_transform import embedding_model
from src.storing.vectore_store import load_the_index
from src.query_model.query_engine_setup import set_llm_model, create_query_engine

def main():

    st.set_page_config("QA ML and AI")

    st.header("QA reagrding Machine Learning and AI")

    user_question = st.text_input("Ask your question")

    if st.button("submit & process"):
        with st.spinner("Processing..."):
            embed_model = embedding_model()
            local_index = load_the_index(embed_model)

            ## set the model
            llm = set_llm_model()
            query_engine = create_query_engine(local_index, llm)

            respose = query_engine.query(user_question)

            st.write(respose.response)

if __name__ == "__main__":
    main()