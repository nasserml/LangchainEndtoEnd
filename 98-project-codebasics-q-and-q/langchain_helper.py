from dotenv import load_dotenv
load_dotenv()
import os
from langchain.document_loaders.csv_loader import CSVLoader
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.llms import GooglePalm
from langchain.vectorstores import FAISS
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA


llm = GooglePalm(google_api_key=os.getenv("GOOGLE_API_KEY"), temperature=0)





instructor_embeddings = HuggingFaceInstructEmbeddings(
    model_name="hkunlp/instructor-base",
    query_instruction = 'Represent the query for retrieval: '
)

vectordb_file_path = 'faiss__index'
def create_vector_db():
    """
    Creates a vector database using the provided CSV file.

    Parameters:
        None

    Returns:
        None
    """
    loader = CSVLoader(file_path='codebasics_faqs.csv', source_column='prompt',encoding='latin-1')
    docs = loader.load()
    vectordb = FAISS.from_documents(documents=docs, embedding=instructor_embeddings)
    vectordb.save_local(vectordb_file_path)
    

def get_qa_chain():
    """
    Generate a retrieval QA chain for querying a vector database using a given context and question.

    Returns:
        chain (RetrievalQA): A retrieval QA chain object that can be used to query the vector database.

    Raises:
        None
    """
    # Load the vector database from the local folder
    vectordb = FAISS.load_local(vectordb_file_path, instructor_embeddings)

    # Create a retriever for querying the vector database
    retriever = vectordb.as_retriever(score_threshold=0.7)

    prompt_template = """Given the following context and a question, generate an answer based on this context only.
    In the answer try to provide as much text as possible from "response" section in the source document context without making much changes.
    If the answer is not found in the context, kindly state "I don't know." Don't try to make up an answer.

    CONTEXT: {context}

    QUESTION: {question}"""

    PROMPT = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    chain = RetrievalQA.from_chain_type(llm=llm,
                                        chain_type="stuff",
                                        retriever=retriever,
                                        input_key="query",
                                        return_source_documents=True,
                                        chain_type_kwargs={"prompt": PROMPT})

    return chain
    
if __name__ == '__main__':
    chain = get_qa_chain()
    print(chain('do you provide intership? do you have EMI option?'))