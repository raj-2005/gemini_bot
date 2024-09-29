import streamlit as st
import requests

# Function to get response from your edge function
def get_gemini_response(query):
    endpoint = "YOUR_EDGE_FUNCTION_URL"  # Replace with your edge function URL

    payload = {
        "query": query
    }

    response = requests.post(endpoint, json=payload)

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
        # Get the response from your edge function
        answer = get_gemini_response(user_input)
        st.text_area("Chatbot Response:", answer, height=200)
    else:
        st.warning("Please enter a question to get an answer.")
