import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Load API Key from .env
genai.configure(api_key=os.getenv("AIzaSyBPw_YrO11qT15Mc2fsHFTGDzMdarYNdQU"))

# Load Gemini model
model = genai.GenerativeModel("gemini-1.5-flash")

def chat_response(question):
    try:
        response = model.generate_content(question)
        return response.text
    except Exception as e:
        return f"Error from Gemini: {e}"
