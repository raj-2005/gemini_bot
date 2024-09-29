import streamlit as st
import requests
import json

# Function to get the Gemini API URL and API Key dynamically
def get_gemini_credentials():
    # Ideally, you would fetch these from environment variables or a secure vault
    api_key = st.secrets["GEMINI_API_KEY"]  # Store your API key securely
    base_url = "https://generativelanguage.googleapis.com/v1beta/models/YOUR_MODEL_NAME:generateContent"  # Change YOUR_MODEL_NAME appropriately
    return base_url, api_key

# Function to get response from Gemini API
def get_gemini_response(query):
    endpoint, api_key = get_gemini_credentials()

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": query,
        "max_output_tokens": 50,  # You can adjust this
        "temperature": 0.7,  # You can adjust this
        "top_p": 0.9,
        "n": 1,
        "stop_sequences": ["\n"]
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get('candidates', [{}])[0].get('output', 'Sorry, I could not understand that.')
    else:
        return "Error: " + response.text

# Streamlit app layout
st.title("Patient Query Chatbot")

# Chat interface
st.subheader("Ask your questions about skin health:")
user_input = st.text_input("Type your question here:")

if st.button("Get Answer"):
    if user_input:
        # Get the response from Gemini
        answer = get_gemini_response(user_input)
        st.text_area("Chatbot Response:", answer, height=200)
    else:
        st.warning("Please enter a question to get an answer.")
