import streamlit as st
import google.generativeai as genai
import os
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
best assistance for improving the Health Condition.
Utilize this information to generate tailored suggestions for food intake and physical activities. Consider factors such as dietary restrictions, calorie needs, nutritional requirements, and suitable exercise routines based on the patient's profileand address any specific health concerns the patient may have  with high accuracy
assign the BMR in calories by taking the inputs from the age, gender, weight, height
age:{age}
gender:{sex}
weight:{kgs}
height:{cms}
health issues:{hi}

I only want the below responses in paragraph format not print patient profile and health issues
{{BMR : ()
    food intake:[],
recommend physical activities to do:,
calorie needs, nutritional requirements :,
dietary restrictions:
 .}}
"""
st.title("HMA")
st.text("Health management Assistance")
age = st.text_area("Enter your age")
sex = st.text_area("Enter your gender")
kgs = st.text_area("Enter your weight(kg's)")
cms = st.text_area("Enter your height(cm's)")
hi = st.text_area("write the condition of you")


submit = st.button("Submit")

if submit:
        response = get_gemini_repsonse(input_prompt)
        st.subheader(response)
