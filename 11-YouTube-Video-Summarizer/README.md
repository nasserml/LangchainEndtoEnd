# YouTube Video Summarizer App

This Streamlit web application uses Google's Gemini Pro AI model to summarize the content of YouTube videos based on their transcripts. The summarizer extracts important details from the video transcript and provides a concise summary within 250 words.

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

Visit the provided link in your browser to access the YouTube Video Summarizer.

## Functionality

### `extract_transcript_details`

```python
def extract_transcript_details(youtube_video_url):
    """
    Extract transcript details from a Youtube video URL

    Args:
        youtube_video_url (str): The URL of the YouTube video.

    Raises:
        Exception: If an error occurs during the extraction process.

    Returns:
        str: The extracted transcript text.
    """
    # Implementation details...
```

### `generate_gemini_content`

```python
def generate_gemini_content(transcript_text, prompt):
    """
    Generates content using the Gemini Pro generative model based on the given transcript text and prompt.

    Args:
        transcript_text (str): The transcript text to be used for content generation.
        prompt (str): The prompt to provide context for the generation.

    Returns:
        str: The generated context text.
    """
    # Implementation details...
```

## Usage

1. Open the app in your browser using the provided link after running the Streamlit command.

2. Enter the YouTube video link in the "Enter the YouTube video link" text field.

3. The YouTube video thumbnail will be displayed.

4. Click the "Get Detailed Notes" button to generate detailed notes based on the video transcript.

5. The app will use Gemini Pro to generate a detailed summary of the video content.

## Important Note

Ensure that you have a valid Google API key for the Gemini Pro model. You can obtain it from the [Google Maker Suite](https://makersuite.google.com/app/).

## Dependencies

- `youtube_transcript_api`
- `streamlit`
- `google-generativeai`
- `python-dotenv`
- `pathlib`

Make sure to replace `"your_google_api_key"` in the `.env` file with your actual Google API key.