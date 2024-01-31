## Health Management APP
from dotenv import load_dotenv ## to load environment variables

load_dotenv() # load all the environment varaiblaes

import streamlit as st # for web development
import os # os is used to interact with the operating system
import google.generativeai as genai # to load google gemini model
from PIL import Image # to load images

genai.configure(api_key=os.getenv("GOOGLE_API-KEY")) # configure api key for google gemini

## Function to load google gemini pro vision Api and get response

def get_gemini_response(input_prompt, image):
    """
    Generates a response using the Gemini Pro Vision generative model.
    
    This function takes in two argements: `input_prompt`, `image`.
    `input_prompt` is the input to be used for genearting the content,
    `image` is a list of images to be used in the generation process, and the 
    
    The function initializes a generative model with the Gemini Pro Vision
    and generates content using the input_prompt, and the first image in the list
    . It then returns the generated text response.

    Args:
        input_prompt (str): The input to be used for generating the content.
        image (list): A list of images to be used in the generation process.

    Returns:
        str: The generated text response.
    """
    # Initiate the generative model with the gemini pro vision
    model = genai.GenerativeModel("gemini-pro-vision")
    
    # Generate content using the input, first image in the list, and the prompt
    response = model.generate_content([input_prompt, image[0]])
    
    # Return the geberated text response
    return response.text


def input_image_setup(uploaded_file):
    """
    Sets up the input image for the Gemini Pro Vision generative model.
    
    This function takes in one argument: `uploaded_file`. It checks if the file
    has been uploaded. If it has, it reads the file into bytes and store it
    in a list of image parts. The function then returns the list of image parts.

    Args:
        uploaded_file (FileStorage): The uploaded file to be used as input.
    Raises:
        FileNotFoundError: if the file has not been uploaded.

    Returns:
        list: A list of image parts containing the mime type and data of the uploaded file.
    """
    # Check if the file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()
        
        # Create a dictionary with the file's MIME type and data
        # This format required by the Gemini Pro Vision
        image_parts = [
            {
                "mime_type": uploaded_file.type, # Get the mime type of the uploaded file
                "data": bytes_data # Get the data of the uploaded file
            }
        ]
        return image_parts # Return the image parts
    else:
        raise FileNotFoundError("Please upload an image") # Return an error if the file has not been uploaded


# Initialize the streamlit app

# Set the page title to "Gemini Health App"
st.set_page_config(page_title="Gemini Health App")

# Set the header to "Gemini Health App"
st.header("Gemini Health App")

# Create a text input field for the user to input the prompt for the model
input = st.text_input("Input Prompt: ", key="input")

# Create a file uploader for the user to upload an image for the model
uploaded_file = st.file_uploader("Choose an image..." , type=["png", "jpg", "jpeg"])

# Initialize the image variable
image = ""

# Check if the user has uploaded an image, open the image and display it
if uploaded_file is not None:
    
    # Open the uploaded image
    image = Image.open(uploaded_file)
    
    # Display the uploaded image in the streamlit app
    st.image(image, caption="Uploaded Image", use_column_width=True)

# Create submit button that calculates the total calories
submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----
               
        Finally you can mention whether the food is healthy or not and also 
        mention the 
        precentage split of the ratio of carbohydrates, fats, fibers, suger and other important
        things required in our diet
"""

# If submit button is clicked
if submit:
    
    # Convert the image to bytes and store it in the image variable
    image_date = input_image_setup(uploaded_file)
    
    # Generate the response using the get_gemini_response function
    response = get_gemini_response(input_prompt, image_date)
    
    # Display subheader and response
    st.subheader("The Response is")
    
    # Display the response
    st.write(response)