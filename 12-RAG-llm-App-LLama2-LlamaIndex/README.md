# RAG System Using LLama2 With Hugging Face

This Jupyter Notebook demonstrates the implementation of a Retrieval-Augmented Generation (RAG) system using the LLama2 language model with Hugging Face's transformers. The system incorporates the LLama2 model for language understanding and generation, Hugging Face for embeddings, and the llama-index library for vector storage and retrieval.

## Installation

Make sure to install the required dependencies using the following commands:

```bash
!pip install pypdf
!pip install -q transformers einops accelerate langchain bitsandbytes
!pip install sentence_transformers
!pip install llama-index==0.9.33
```

## Usage

1. **Login to Hugging Face**: Run the following command to log in to your Hugging Face account:

```python
!huggingface-cli login
```

2. **Initialize LLama2 with Hugging Face LLM**:

```python
import torch
from llama_index.llms import HuggingFaceLLM
from llama_index.prompts.prompts import SimpleInputPrompt

system_prompt = """
You are a Q&A assistant. Your goal is to answer questions as
accurately as possible based on the instructions and context provided.
"""

query_wrapper_prompt = SimpleInputPrompt("{query_str}")

llm = HuggingFaceLLM(
    context_window=4096,
    max_new_tokens=256,
    generate_kwargs={"temperature": 0.0, "do_sample": False},
    system_prompt=system_prompt,
    query_wrapper_prompt=query_wrapper_prompt,
    tokenizer_name="NousResearch/Llama-2-7b-chat-hf",
    model_name="NousResearch/Llama-2-7b-chat-hf",
    device_map="auto",
    # uncomment this if using CUDA to reduce memory usage
    model_kwargs={"torch_dtype": torch.float16, "load_in_8bit": True}
)
```

3. **Initialize Embedding Model**:

```python
from langchain.embeddings.huggingface import HuggingFaceBgeEmbeddings
from llama_index import ServiceContext
from llama_index.embeddings import LangchainEmbedding

embed_model = LangchainEmbedding(HuggingFaceBgeEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2"))

service_context = ServiceContext.from_defaults(
    chunk_size=1024,
    llm=llm,
    embed_model=embed_model
)
```

4. **Vector Storage and Querying**:

```python
from llama_index import VectorStoreIndex, SimpleDirectoryReader

# Load documents from the specified directory
documents = SimpleDirectoryReader("/content/data").load_data()

# Create an index with the loaded documents and service context
index = VectorStoreIndex.from_documents(documents, service_context=service_context)

# Create a query engine from the index
query_engine = index.as_query_engine()

# Query the system
response = query_engine.query("what is attention?")
print(response)
```

5. **Sample Queries**:

```python
# Sample query 1
response = query_engine.query("what is YOLO?")
print(response)
```

