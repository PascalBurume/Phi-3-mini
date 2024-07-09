import streamlit as st
import json
import urllib.request
import urllib.error
import os
import ssl

# Function to allow self-signed HTTPS certificates
def allowSelfSignedHttps(allowed):
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context

allowSelfSignedHttps(True)

# Set page title
st.set_page_config(page_title="Phi-3-mini-128k", page_icon="🤖", layout="centered", initial_sidebar_state="expanded")

# Title and introduction
st.title("Phi-3-mini-128k-instruct ")
st.image("microsoft.jpg", width=500)
st.markdown(""" 
    Phi-3-mini is a groundbreaking language model developed by Microsoft.
    Despite its small size, it introduces top-tier AI technology to smartphones, enhancing functionality without relying on cloud computing. 
    This compact model demonstrates outstanding results in AI benchmarks, showcasing its ability to efficiently manage complex tasks and language processing.
    Phi-3-mini is equivalent in performance to larger language models while being small enough to be deployed directly on your phone. 
    It’s a game-changer for mobile AI capabilities! 😊
""")

# Initialize chat history and token usage
if "phi3_chat_history" not in st.session_state:
    st.session_state.phi3_chat_history = []

# Initialize tokens used
if "tokens_used" not in st.session_state:
    st.session_state.tokens_used = 0
else:
    st.session_state.tokens_used = 0  # Reset tokens used for new session

# Sidebar to show tokens used and adjust parameters
with st.sidebar:
    st.title('📡 🌐 Phi-3-mini-128k')
    st.write('This chatbot is created using the open-source Phi-3 model from Microsoft.')
    st.success('API key already provided!', icon='✅')

    temperature = st.slider('Temperature', min_value=0.01, max_value=1.0, value=0.7, step=0.01)
    top_p = st.slider('Top P', min_value=0.01, max_value=1.0, value=1.0, step=0.01)
    max_length = st.slider('Max Length', min_value=32, max_value=1024, value=1024, step=8)
    st.markdown(f"**Tokens Used:** {st.session_state.tokens_used}")

# Clear chat button
    if st.button("Clear Chat"):
        st.session_state.phi3_chat_history = []
        st.session_state.tokens_used = 0
        st.session_state.phi3_chat_history.append(
            {"inputs": {"chat_input": None},
             "outputs": {"chat_output": "How can I help you?"}}
        )
# Display chat history
for interaction in st.session_state.phi3_chat_history:
    if interaction["inputs"]["chat_input"]:
        with st.chat_message("user"):
            st.write(interaction["inputs"]["chat_input"])
    if interaction["outputs"]["chat_output"]:
        with st.chat_message("assistant"):
            st.write(interaction["outputs"]["chat_output"])

# React to user input
user_input = st.chat_input("Ask me everything...")
if user_input:
    # Display user message in chat message container
    st.chat_message("user").markdown(user_input)
    
    # Adding user input to the default messages
    default_messages = []  # Define your default messages here
    data = {
        "messages": default_messages + [{"role": "user", "content": user_input}],
        "max_tokens": max_length,
        "temperature": temperature,
        "top_p": top_p
    }

    # Convert data to JSON string
    body = str.encode(json.dumps(data))

    # API endpoint
    url = 'https://Phi-3-medium-4k-instruct-hbcck-serverless.swedencentral.inference.ai.azure.com/v1/chat/completions'
    api_key = 'sginPuVLYGfaNPch5QXoHjmoYaDh42gw'  # Replace with your actual API key

    if not api_key:
        st.error("A key should be provided to invoke the endpoint")
    else:
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + api_key}

        req = urllib.request.Request(url, body, headers)

        try:
            response = urllib.request.urlopen(req)
            result = response.read()
            response_data = json.loads(result.decode('utf-8'))

            # Check if 'choices' key exists in the response_data
            if 'choices' in response_data and response_data['choices']:
                chat_output = response_data['choices'][0]['message']['content']
                with st.chat_message("assistant"):
                    st.markdown(chat_output)

                st.session_state.phi3_chat_history.append(
                    {"inputs": {"chat_input": user_input},
                     "outputs": {"chat_output": chat_output}}
                )

                # Update tokens used
                if "usage" in response_data:
                    st.session_state.tokens_used = response_data["usage"].get("total_tokens", 0)
                st.sidebar.markdown(f"**Tokens Used:** {st.session_state.tokens_used}")

            else:
                st.error("The response data does not contain a valid 'choices' key or it's empty.")

        except urllib.error.HTTPError as error:
            st.error(f"The request failed with status code: {error.code}")
            st.error(error.info())
            st.error(error.read().decode("utf8", 'ignore'))
        except urllib.error.URLError as error:
            st.error(f"Failed to reach the server: {error.reason}")
        except json.JSONDecodeError:
            st.error("Failed to decode the JSON response.")
        except Exception as e:
            st.error(f"An unexpected error occurred: {str(e)}")
