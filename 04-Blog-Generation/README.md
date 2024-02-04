# Blog Generation with LLama 2

This Streamlit application leverages the LLama 2 language model from CTransformers to generate blogs based on user input. The LLama 2 model is fine-tuned for chat-like interactions and can be prompted to create blog content within specified parameters.

## Functionality

The `getLLamaresponse` function utilizes the LLama 2 model to generate a blog response based on user-provided input such as the blog topic, desired word count, and writing style.

```python
response = getLLamaresponse(input_text, no_words, blog_style)
```

## LLama 2 Model and Prompt Template

The LLama 2 model is loaded using CTransformers with specific configuration parameters. The input for generating the response is constructed using a prompt template that incorporates the user-provided variables.

```python
llm = CTransformers(model='models/llama-2-7b-chat.ggmlv3.q8_0.bin',
                    model_type='llama',
                    config={'max_new_tokens': 256, 'temperature': 0.01})

template = """
    Write a blog for {blog_style} job profile for a topic {input_text}
    within {no_words} words.
        """
prompt = PromptTemplate(input_variables=["blog_style", "input_text", 'no_words'],
                        template=template)
```

## Streamlit User Interface

The Streamlit app provides a simple user interface for entering the blog topic, selecting the writing style, and specifying the desired word count. The generated blog can be obtained by clicking the "Generate" button.

```python
input_text = st.text_input("Enter the Blog Topic")

col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                             ('Researchers', 'Data Scientist', 'Common People'), index=0)

submit = st.button("Generate")

if submit:
    st.write(getLLamaresponse(input_text, no_words, blog_style))
```

## Requirements

Make sure to install the required dependencies using the following:

```bash
pip install sentence-transformers uvicorn ctransformers langchain python-box streamlit
```

