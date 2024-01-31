

# Health Management App

## Overview

This is a Health Management App powered by the Gemini Pro Vision generative model. The app allows users to input a prompt and upload an image of food items. It then utilizes the generative model to provide a detailed response, including the total calories, individual food item details, and nutritional information.

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
streamlit run health.py
```

Visit the provided link in your browser to access the Health Management App.

## Functionality

### `get_gemini_response`

```python
def get_gemini_response(input_prompt, image):
    """
    Generates a response using the Gemini Pro Vision generative model.
    
    Args:
        input_prompt (str): The input to be used for generating the content.
        image (list): A list of images to be used in the generation process.

    Returns:
        str: The generated text response.
    """
    # Implementation details...
```

### `input_image_setup`

```python
def input_image_setup(uploaded_file):
    """
    Sets up the input image for the Gemini Pro Vision generative model.
    
    Args:
        uploaded_file (FileStorage): The uploaded file to be used as input.

    Returns:
        list: A list of image parts containing the mime type and data of the uploaded file.
    """
    # Implementation details...
```

## Usage

1. Open the app in your browser using the provided link after running the Streamlit command.

2. Enter a prompt in the "Input Prompt" text field.

3. Upload an image containing food items using the file uploader.

4. Click the "Tell me the total calories" button.

5. The app will generate a response with details on the total calories, individual food items, and nutritional information.

## Important Note

Ensure that you have a valid Google API key for the Gemini Pro Vision model. You can obtain it from the [Google Maker Suite](https://makersuite.google.com/app//).

## Dependencies

- `streamlit`
- `google-generativeai`
- `python-dotenv`
- `langchain`
- `PyPDF2`
- `chromadb`
- `pdf2image`
- `faiss-cpu`
- `langchain_google_genai`
```
Make sure to replace `"your_google_api_key"` in the `.env` file with your actual Google API key. Additionally, update the `Implementation details...` in the function docstrings with the actual implementation logic for your application.