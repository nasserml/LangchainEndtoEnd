import streamlit as st  # for web development
from dotenv import load_dotenv # to load environment variables

load_dotenv() # load all the environment variables

import google.generativeai as genai # to load google gemini ai model
import os # is used to interact with the operating system

from youtube_transcript_api import YouTubeTranscriptApi # to ectract transcript from youtube video

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # configure api key for google gemini ai model

prompt = """You are Yotube video summarizer. You will be taking the transcript text
and summarizing the entire video and providing the important summary in points
within 250 words. Please provide the summary of the text given here:  """  # Prompt for the summarizer

# getting the transcript data from youtube videos
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
    try:
        
        video_id = youtube_video_url.split("=")[1] # Get the youtube video id from the url
        
        transcript_text = YouTubeTranscriptApi.get_transcript(video_id) # Get the transcript text from the youtube video
        
        transcript = "" # Initialize the transcript
        
        for i in transcript_text:
            transcript += " " + i["text"] # Add the transcript text to the transcript variable
        
        return transcript # Return the transcript text
    
    except Exception as e:  # If an error occurs then raise the error
        raise e # Raise the error 
    


def generate_gemini_content(transcript_text, prompt):
    """
    Generates content using the Gemini Pro generative model based on the given transcript text and prompt.

    Args:
        transcript_text (str): The transcript text to be used for content generation.
        prompt (str): The prompt to provide context for the generation.

    Returns:
        str: The generated context text.
    """
    
    model = genai.GenerativeModel("gemini-pro") # Initiate the generative model with the gemini pro
    
    response = model.generate_content(prompt + transcript_text) # Generate content using the prompt and transcript text
    
    return response.text # Return the generated text 

st.title("YouTube Transcript to Detailed Note Converter") # Title of the web app

youtube_link = st.text_input("Enter the YouTube video link: ") # Text input for the youtube link

if youtube_link: # If the youtube link is entered 
    
    video_id = youtube_link.split("=")[1] # Get the youtube video id from the url 
    
    st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True) # Display the youtube video thumbnail

if st.button("Get Detailed Notes"): # If the button is clicked
    
    transcript_text = extract_transcript_details(youtube_link) # Get the transcript text from the youtube video
    
    if transcript_text: # If the transcript text is not empty
        
        summary = generate_gemini_content(transcript_text, prompt) # Generate the summary from the transcript text based on the prompt
        
        st.markdown("## Detailed Notes:") # Display string formatted as Markdown.
        
        st.write(summary) # Display the summary