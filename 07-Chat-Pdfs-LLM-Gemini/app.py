import streamlit as st 
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from langchain.vectorstores import FAISS
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv



load_dotenv()
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_pdf_text(pdf_docs: list) -> str:
    """
    Generate a text from a list of pdf documents.
    
    Args:
        pdf_docs (list): A list of pdf documents.

    Returns:
        str: The concatenated text extracted from all the pages of the PDF documents.
    """
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text+=page.extract_text()
    return text

def get_text_chunks(text: str) -> list:
    """
    Generate a list of text chunks.

    Args:
        text (str): The text to be splitted into chuncks.

    Returns:
        list: A list of text chuncks.
    """
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks


def get_vector_store(text_chunks: list[str]):
    """
    Generate a vector store from a list of text chunks.

    Args:
        text_chunks (list[str]): A list of text chunks.
    
    Returns:
        None
    """
    # embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    # vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    
    # vector_store.save_local("faiss_index")
    
    embeddings_instance = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    # Assuming FAISS.from_texts takes an Embeddings instance directly
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings_instance)
    vector_store.save_local("faiss_index")


def get_conversational_chain():
    """
    Return a conversational chain that can be used to answer questions based on a given context and question.
    
    Parameters:
        None
    
    Returns:
        chain (object): A conversational chain object that can be used to answer questions based on a given context and question.
    """
    prompt_template = """
    Answer the question as detailed as possible from the provided context, make sure to provide all the details, if the answer is not in
    provided context just say, "answer is not available in the context", don't provide the wrong answer\n\n
    Context:\n {context}?\n
    Question: \n{question}\n

    Answer:
    
    """
    model=ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
    PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    chain = load_qa_chain(model, chain_type="stuff", prompt=prompt_template)
    return chain

def user_input(user_question):
    """
    Generate a response to a user question using a generative AI model.

    Args:
        user_question (str): The question asked by the user.
    
    Returns:
        None
    """
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    new_db = FAISS.load_local("faiss_index", embeddings)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    
    response = chain(
        {"input_documents":docs, "question": user_question}
        , return_only_outputs=True)

    print(response)
    st.write("Reply: ", response["output_text"])


def main():
    st.set_page_config("Chat With Multiple PDF")
    st.header("Chat with Multiple PDF using Gemini💁")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader("Upload your PDF Files and Click on the Submit & Process Button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Done")



if __name__ == "__main__":
    main()