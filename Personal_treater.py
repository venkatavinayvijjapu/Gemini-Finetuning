from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import os
import google.generativeai as genai 
from PIL import Image

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def gemini_res(input,image,prompt):
    model=genai.GenerativeModel('gemini-pro-vision')
    res=model.generate_content([input,image[0],prompt])
    return res.text

def input_img(upload_file):
    if upload_file is not None:
        bytes_data=upload_file.getvalue()
        image_parts=[{
                "mime_type":upload_file.type,
                "data":bytes_data
        }
        ]
        return image_parts
    else:
        return FileNotFoundError("No File exist")
    
input=st.text_input("Input_Prompt:",key="Input")
upload_file=st.file_uploader("Choose a image...",type=['jpg','jpeg','png'])
image=""
if upload_file is not None:
    image=Image.open(upload_file)
    st.image(image=image,caption="uploaded Image",use_column_width=True)
submit=st.button("Tell me the total calories")

input_prompt="""
You are an expert in nutritionist where you need to see the food items from the image
               and calculate the total calories, also provide the details of every food items with calories intake
               is below format

               1. Item 1 - no of calories
               2. Item 2 - no of calories
               ----
               ----


"""

## If submit button is clicked

if submit:
    image_data=input_img(upload_file)
    response=gemini_res(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)

