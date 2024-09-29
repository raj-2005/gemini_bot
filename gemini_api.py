import streamlit as st
import requests

# Function to get response from Gemini API
def get_gemini_response(query):
    api_key = "YOUR_API_KEY"  # Replace with your actual Gemini API key
    endpoint = "https://generativelanguage.googleapis.com/v1beta/models/text-bison:generateText"  # Suggested endpoint

    headers = {
        "Authorization": f"Bearer {api_key}",  # Use the correct variable for the API key
        "Content-Type": "application/json"
    }

    payload = {
        "prompt": query,
        "temperature": 0.5,
        "maxOutputTokens": 256,
        "topP": 0.8,
        "topK": 40,
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get('candidates', [{}])[0].get('text', 'Sorry, I could not understand that.')
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
