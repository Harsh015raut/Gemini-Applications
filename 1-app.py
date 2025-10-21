import os 
import google.generativeai as genai 
import streamlit as st 
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load Gemini Pro model and get responses 

model = genai.GenerativeModel("gemini-2.5-flash")

def get_gemini_respone(question):
    response = model.generate_content(question)
    return response.text 

# Initialize streamlit app 

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")

input = st.text_input("Input: ", key="input")
submit = st.button("Ask the question")

# When submit button is clicked 

if submit:
    response = get_gemini_respone(input)
    st.subheader("The Response is")
    st.write(response)