import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  ## load all our environment variables

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_repsonse(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text


def input_pdf_text(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in range(len(reader.pages)):
        page = reader.pages[page]
        text += str(page.extract_text())
    return text


# Prompt Template

# I want the response in one single string having the structure

input_prompt = """
Hey Act Like a skilled or very experience HMA(Health Management Assistence)
with a deep understanding of nutrition, physcial excersises, food and humans health conditions
. Your task is to evaluate the Health condition based on the given Patient Profile.
You must consider the Healthcare is very competitive and you should provide 
best assistance for improving the Health Condition.
Utilize this information to generate tailored suggestions for food intake and physical activities. Consider factors such as dietary restrictions, calorie needs, nutritional requirements, and suitable exercise routines based on the patient's profileand address any specific health concerns the patient may have  with high accuracy
assign the BMR in calories by taking the inputs from the Patient Profile
Patient Profile:{text}
health issues:{jd}

I only want the below responses in paragraph format not print patient profile and health issues
{{BMR : ()
    food intake:[],
recommend physical activities to do:,
calorie needs, nutritional requirements :,
dietary restrictions:
 .}}
"""

## streamlit app
st.title("HMA")
st.text("Health management Assistance")
jd = st.text_area("write the condition of you")
uploaded_file = st.file_uploader(
    "Upload Your profile", type="pdf", help="Please uplaod the pp"
)

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_repsonse(input_prompt)
        st.subheader(response)
