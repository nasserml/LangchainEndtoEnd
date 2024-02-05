
# Resume ATS Tracker

This Streamlit web application leverages the Gemini Pro generative model to evaluate resumes based on a given job description. The application acts as a skilled Application Tracking System (ATS) with a deep understanding of the tech field, including software engineering, data science, data analysis, and big data engineering.

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
streamlit run app.py
```

Visit the provided link in your browser to access the Resume ATS Tracker.

## Functionality

### `get_gemini_response`

```python
def get_gemini_response(input):
    """
    Generates a response using the Gemini Pro generative model.

    Args:
        input (str): The input to generate content from.

    Returns:
        str: The generated content.
    """
    # Implementation details...
```

### `input_pdf_text`

```python
def input_pdf_text(uploaded_file):
    """
    Extracts text from a PDF file.

    Args:
        uploaded_file (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF file.
    """
    # Implementation details...
```

## Usage

1. Open the app in your browser using the provided link after running the Streamlit command.

2. Enter the job description in the text area.

3. Upload your resume in PDF format using the file uploader.

4. Click the "Submit" button to evaluate your resume based on the provided job description.

5. The app will generate a response indicating the percentage match with the job description, missing keywords, and profile summary.

## Important Note

Ensure that you have a valid Google API key for the Gemini Pro model. You can obtain it from the [Google Maker Suite](https://makersuite.google.com/app/).

## Dependencies

- `streamlit`
- `PyPDF2`
- `google.generativeai`
- `python-dotenv`
 

Make sure to replace `"your_google_api_key"` in the `.env` file with your actual Google API key. Additionally, update the `Implementation details...` in the function docstrings with the actual implementation logic for your application.