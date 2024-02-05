import streamlit as st # for web development
import google.generativeai as genai # to load google gemini ai model
import os # is used to interact with the operating system
import PyPDF2 as pdf # to read pdf files and extract text

from dotenv import load_dotenv # to load enviroment variables

load_dotenv() # load all the environment variables from the .env file

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # configure api key for google gemini ai model

# Gemini Pro response
def get_gemini_response(input):
    """
    Generates response using the Gemini Pro generative model.

    Args:
        input (str): The input to generate content from.

    Returns:
        str: The generated content فثءف.
    """
    
    # Initiate the generative model with the gemini pro
    model = genai.GenerativeModel("gemini-pro") 
    
    # Generate content using the input
    response = model.generate_content(input) 
    
    # Return the generated text response
    return response.text

def input_pdf_text(uploaded_file):
    """
    Extract text from a PDF file.

    Args:
        uploaded_file (str): Path to the PDF file.

    Returns:
        str: Extracted text from the PDF file.
    """
    # Read the pdf file
    reader = pdf.PdfReader(uploaded_file)
    
    # Initialize the text variable to an empty string
    text = ""
    
    # Extract text from each page
    for page in range(len(reader.pages)):
        
        # Extract text from the page
        page = reader.pages[page]
        
        # Add the extracted text to the text variable
        text += str(page.extract_text())
    
    # Return the text 
    return text


input_prompt="""
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{jd}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}
"""

# streamlit app
st.title("Resume ATS Tracker") # Title of the web app

st.text("Improve Your Resume ATS") 

jb = st.text_area("Enter Job Description: ") # Text input for the job description

uploaded_file = st.file_uploader("Upload Your Resume", type="pdf" , help="Please upload the pdf") # File uploader for the resume

submit = st.button("Submit") # Submit button

if submit: # If the submit button is clicked
    
    if uploaded_file  is not None: # If file is uploaded
        
        text = input_pdf_text(uploaded_file) # Extract text from the pdf
        
        response = get_gemini_response(input_prompt) # Generate response using the gemini pro model
        
        st.subheader(response) # Display the response