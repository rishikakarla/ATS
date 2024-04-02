import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  ## load all our environment variables

genai.configure(api_key=os.getenv("AIzaSyAZNiLH-wqNPkl1OtPRkD0BqMPeCAM1gjE"))


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
Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. 
Profile summary must be based on the resume, not job description. Assign the percentage Matching based 
on Jd and the missing keywords with high accuracy. 
Give the existing jobs that matches the profile and can be applied.
do not create any. Check the skills required and correctly with high accuracy
resume:{text}
description:{jd}

I want the below response in Headings and details format

{{"Role Match":"%",
"MissingKeywords:[]",
"Profile Summary":"",
"Jobs matches with their links":"",
"recommend courses to learn with links":"",
"resources for skill improvement (Give certifications)":""
"possible resume change":""}}
"""

## streamlit app
st.title("Smart ATS")
st.text("Improve Your Resume ATS")
jd = st.text_area("Paste the Job Description")
uploaded_file = st.file_uploader(
    "Upload Your Resume", type="pdf", help="Please uplaod the pdf"
)

submit = st.button("Submit")

if submit:
    if uploaded_file is not None:
        text = input_pdf_text(uploaded_file)
        response = get_gemini_repsonse(input_prompt)
        st.subheader(response)
