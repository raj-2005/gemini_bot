#!/usr/bin/env python
# coding: utf-8

import streamlit as st
import requests

# Function to get response from Gemini API
def get_gemini_response(query):
    api_key = "AIzaSyCm2k__h6OqV0SwywgVW6YyYlGWX2zk4Xw"  # Replace with your Gemini API key
    endpoint = "https://api.gemini.com/v1/chat"  # Use the correct endpoint for Gemini API

    headers = {
        "Authorization": f"Bearer {api_key}",  # Use the correct variable for the API key
        "Content-Type": "application/json"
    }

    payload = {
        "query": query
    }

    response = requests.post(endpoint, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get('response', 'Sorry, I could not understand that.')
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





