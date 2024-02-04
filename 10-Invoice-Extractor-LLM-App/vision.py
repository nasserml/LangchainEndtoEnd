

from dotenv import load_dotenv # to load environment variables

load_dotenv() # laod all the environment variables from .env file and load GOOGLE_API_KEY

import streamlit as st # for the web development using streamlit
import os # is used to interact with the operating system
from PIL import Image # to load images

import google.generativeai as genai # to load google gemini ai model 

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) # configure api key for google gemini ai model

# Fucntion to load google gemini pro vision Api and get response 

model = genai.GenerativeModel("gemini-pro-vision") # Initiate the generative model with the gemini pro vision

def get_gemini_response(input, image, prompt):
    """
    Generates a response from the Gemini Pro Vision using the input text, the first image, and the prompt text.

    Args:
        input (str): The input prompt to provide context for the generation.
        image (list): A list of images to be used in the generation process.
        prompt (str): The prompt text.

    Returns:
        str: Thee generated text response.
    """
    # Generate content using input, the first image, and the prompt
    response = model.generate_content([input, image[0], prompt])
    
    # Return the generated text response
    return response.text



def input_image_setup(uploaded_file):
    """
    Set up the input image for the gemini pro vision generative model.

    Args:
        uploaded_file (FileStorage): The uploaded file to be used as input.

    Raises:
        FileNotFoundError: If no file is uploaded.

    Returns:
        list: A list of image parts containing the mime type and date of the uploaded file.
    """
    # Check if the file has been uploaded
    if uploaded_file is not None:
        
        bytes_data = uploaded_file.getvalue() # Read the file into bytes
        
        image_parts = [{
            "mime_type": uploaded_file.type, # Get the mime type of the uploaded file
            "data": bytes_data # Get the data of the uploaded file
        }]
        
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded") # Raise an error if no file is uploaded


# initialize our streamlit app

st.set_page_config(page_title="Multi language Invoice Extractor") # set the page title for the app

st.header("Multi language Invoice Extractor") # header for the app

input = st.text_input("Input Prompt: " , key="input") # input text to be used for genearting the content

uploaded_file = st.file_uploader("Choose an image of the invoice...", type=["jpg", "jpeg", "png"]) # upload image file to be used in the generation process

image = "" # variable to store the image

# if image is uploaded then display the image
if uploaded_file is not None:
    
    # open the image file and store in the image variable
    image = Image.open(uploaded_file)
    
    # display the image in the web app
    st.image(image, caption="Uploaded Invoice", use_column_width=True)


submit = st.button("Tell me about the invoice") # submit button to generate the content using the input text, the first image, and the prompt

# input prompt
input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

# if submit button is clicked
if submit:
    
    image_data = input_image_setup(uploaded_file) # set up the input image for the gemini pro vision generative model
    
    response = get_gemini_response(input_prompt, image_data, input) # generate the content using the input text, the first image, and the prompt
    
    st.subheader("The Response is") # subheader for the response in the web app 
    
    st.write(response)  # display the response in the web app 
    