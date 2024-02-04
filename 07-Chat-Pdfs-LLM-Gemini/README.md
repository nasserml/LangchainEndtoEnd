# Chat-Pdfs-LLM-Gemini App

## Overview

The "Chat with Multiple PDF using Gemini" app allows users to engage in conversational queries with multiple PDF documents. Powered by Google Gemini Pro model and LangChain, this Streamlit application extracts text from uploaded PDF files, processes and indexes the content, and enables users to ask questions about the provided context.

## Configuration

1. Install the required libraries listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up your environment variables by creating a `.env` file and adding your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Application Structure

- `app.py`: The main Streamlit app file that allows users to upload PDF files, ask questions, and receive conversational responses.
- `models/`: Directory containing embedding models used for vectorization.
- `faiss_index/`: Directory to store the generated FAISS index.

## Functionality

1. **Text Extraction from PDF (`get_pdf_text`):**
   - The `get_pdf_text` function extracts text from a list of PDF documents using the PyPDF2 library.

2. **Text Chunking (`get_text_chunks`):**
   - The `get_text_chunks` function splits the extracted text into chunks using LangChain's `RecursiveCharacterTextSplitter`.

3. **Vector Store Creation (`get_vector_store`):**
   - The `get_vector_store` function creates a vector store using FAISS from the text chunks and saves it locally.

4. **Conversational Chain Setup (`get_conversational_chain`):**
   - The `get_conversational_chain` function sets up a conversational chain for answering questions based on a given context and question.

5. **User Input Processing (`user_input`):**
   - The `user_input` function generates a response to a user's question using a generative AI model and displays the result.

6. **Main Streamlit App (`main`):**
   - The main Streamlit app includes a text input for users to ask questions.
   - Users can upload multiple PDF files, and the app processes the content to allow for conversational queries.
   - The sidebar provides file upload functionality and a button to trigger processing.

## Running the Application

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Interact with the app by asking questions and uploading PDF files.

3. The app will process the PDF files, create a vector store, and allow users to receive conversational responses based on their queries.

