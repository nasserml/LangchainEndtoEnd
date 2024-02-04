# LangChain Document Processing

This repository demonstrates the use of various libraries and tools for processing and analyzing documents. The main focus is on extracting information from a collection of PDF documents, dividing them into chunks, and performing semantic embeddings with OpenAI's language model. Additionally, it utilizes Pinecone for vector storage and retrieval.

## Requirements
Make sure you have the following dependencies installed:
- tiktoken
- pinecone-client
- pypdf
- openai
- langchain
- pandas
- numpy
- python-dotenv

Install the dependencies using the following:
```bash
pip install tiktoken pinecone-client pypdf openai langchain pandas numpy python-dotenv
```

## Setup

1. Clone the repository:

```bash
git clone https://github.com/nasserml/LangchainEndtoEnd.git
cd cd LangchainEndtoEnd/03-LLM-Generic-App/
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your OpenAI API key:

```bash
OPEN_API_KEY=your_openai_api_key
```

## Document Processing

### Reading Documents

The `read_doc` function loads PDF documents from a specified directory using LangChain's `PyPDFDirectoryLoader`.

```python
doc = read_doc('documents/')
```

### Chunking Documents

The `chunck_data` function divides the loaded documents into chunks using LangChain's `RecursiveCharacterTextSplitter`.

```python
documents = chunck_data(docs=doc)
```

### Embedding Technique with OpenAI

The repository uses OpenAI's language model for text embeddings. Ensure your OpenAI API key is set in the environment variable.

```python
embeddings = OpenAIEmbeddings(api_key=os.environ['OPEN_API_KEY'])
vectors = embeddings.embed_query('How are you')
```

### Vector Search in Pinecone

The vectors are then stored and retrieved using Pinecone. Make sure to initialize Pinecone with your API key.

```python
pinecone.init(api_key='your_pinecone_api_key', environment='gcp-starter')
index_name = 'langchain-vector'
index = Pinecone.from_documents(doc, embeddings, index_name=index_name)
```

### Retrieving Answers

The repository includes a question-answering chain using LangChain and OpenAI's model.

```python
answer = retrieve_answers("How much the agriculture target will be increased by how many crore?")
print(answer)
```

## Additional Requirements

- `tiktoken`: A tool for counting tokens in a text string without making an API call.
- `pinecone-client`: Python client for interacting with the Pinecone vector database.
- `pypdf`: A library for reading PDF files.
- `openai`: OpenAI Python library for interfacing with OpenAI's GPT models.
- `langchain`: LangChain library for various natural language processing tasks.
- `pandas`: Data manipulation library.
- `numpy`: Numerical computing library.
- `python-dotenv`: Library for reading variables from `.env` files.

Make sure to install these requirements using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```
