import streamlit as st
import google.generativeai as genai
import os
import PyPDF2 as pdf
from dotenv import load_dotenv
import json

load_dotenv()  

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_repsonse(input):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(input)
    return response.text



input_prompt = """
Hey Act Like a skilled or very experience HMA(Health Management Assistence)
with a deep understanding of nutrition, physcial excersises, food and humans health conditions
. Your task is to evaluate the Health condition based on the given Patient Profile.
You must consider the Healthcare is very competitive and you should provide 
best assistance for improving the Health Condition.Utilize this information to generate tailored suggestions for BMR of patient and food intake and physical activities. Consider factors such as dietary restrictions, calorie needs, nutritional requirements, and suitable exercise routines based on the given age,height, weight, gender, health condition and allergies and address any specific health concerns the patient may have and profile summary with high accuracy.
Patient Age:{age}
patient height:{ln}
patient weight:{kg}
patient Gender:{sex}
Patient health condition/allergies:{hd}


I want the below response in paragraph format 
{{
"**BMR:[]**",
"food intake:[]",
"Profile Summary":"",
"recommend physical activities to do":"",
"calorie needs, nutritional requirements ":"",
"dietary restrictions":"",}}
"""

st.title("Smart HMA")
age = st.text_area("Age")
ln = st.text_area("Height")
kg = st.text_area("Weight")
sex = st.text_area("Gender")
hd = st.text_area("Health Conditions/Allergies")
submit = st.button("Submit")
