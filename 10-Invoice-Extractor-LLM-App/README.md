
# Multi-Language Invoice Extractor

This is a Streamlit web application for extracting information from invoices using the Gemini Pro Vision generative model.

## Setup

1. Install the required dependencies listed in `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

2. Set up your environment variables by creating a `.env` file and adding your Google API key:

    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Running the App

Run the app using Streamlit:

```bash
streamlit run vision.py
```

Visit the provided link in your browser to access the Multi-Language Invoice Extractor.

## Functionality

### `get_gemini_response`

```python
def get_gemini_response(input_prompt, image, prompt):
    """
    Generates a response from the Gemini Pro Vision using the input text, the first image, and the prompt text.

    Args:
        input_prompt (str): The input prompt to provide context for the generation.
        image (list): A list of images to be used in the generation process.
        prompt (str): The prompt text.

    Returns:
        str: The generated text response.
    """
    # Implementation details...
```

### `input_image_setup`

```python
def input_image_setup(uploaded_file):
    """
    Set up the input image for the Gemini Pro Vision generative model.

    Args:
        uploaded_file (FileStorage): The uploaded file to be used as input.

    Raises:
        FileNotFoundError: If no file is uploaded.

    Returns:
        list: A list of image parts containing the mime type and data of the uploaded file.
    """
    # Implementation details...
```

## Usage

1. Open the app in your browser using the provided link after running the Streamlit command.

2. Enter an input prompt in the "Input Prompt" text field.

3. Upload an image of the invoice using the file uploader.

4. Click the "Tell me about the invoice" button.

5. The app will generate a response based on the input text, uploaded image, and prompt.

## Important Note

Ensure that you have a valid Google API key for the Gemini Pro Vision model. You can obtain it from the [Google Maker Suite](https://makersuite.google.com/app/).

## Dependencies

- `streamlit`
- `google-generativeai`
- `python-dotenv`
- `langchain`
- `PyPDF2`
- `chromadb`
- `faiss-cpu`


Make sure to replace `"your_google_api_key"` in the `.env` file with your actual Google API key. Additionally, update the `Implementation details...` in the function docstrings with the actual implementation logic for your application.