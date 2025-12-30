import streamlit as st
from openai import OpenAI


import streamlit as st
st.set_page_config(page_title="Poet Writer")
st.title('Poet Writer')

openai_api_key = st.sidebar.text_input('OpenAI API Key')


# Initializing the OpenAI client with API key from input
client = OpenAI(api_key=openai_api_key)


# Ensuring that the OpenAI model is set in the session state; defaulting to 'gpt-3.5-turbo'
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = "gpt-3.5-turbo"

user_input = st.text_area("Enter your text here", height=200)


# Create a button to send the input to OpenAI
if st.button('Send to the Bard'):
    
    if not openai_api_key.startswith('sk-'):
        st.warning('Enter your OpenAI API key', icon='⚠')
    
    if user_input and openai_api_key.startswith('sk-'):
        # Make an API call to OpenAI with the user input

        bard_request = "Rewrite this in iambic pentameter. " +user_input

        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
            {"role": "system", "content": "You are an expert poet and writer."},
            {"role": "user", "content": bard_request}
  ]
)
        
        # Display the OpenAI response
        st.write("**Now in Iambic Pentameter 🪄**")
        st.write(completion.choices[0].message.content)
