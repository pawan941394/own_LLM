import streamlit as st
import requests

# Streamlit Header
st.header("Try LLMS ---")

# Dropdown to select model
model = st.selectbox(label='Select LLM', options=['mistral-nemo', 'falcon:40b', 'mistral', 'llama3.1'])

# Chat input
user_input = st.chat_input("Type your message here...")

# Function to get response from API
def get_response(model_name, user_message):
    url = "https://alglc0gfd4latj-11434.proxy.runpod.net/v1/chat/completions"
    headers = {
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model_name,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message}
        ]
    }
    response = requests.post(url, headers=headers, json=data)
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        return f"Error: {response.status_code} - {response.text}"

# Display the response when user input is provided
if user_input:
    response = get_response(model, user_input)
    st.write("Response:", response)
