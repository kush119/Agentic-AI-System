import streamlit as st
import requests
import json

st.title("Agentic AI Assistant")

# Backend URL configuration
BACKEND_URL = "http://localhost:8000/chat"

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What would you like to ask?"):
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # Send request to backend
                response = requests.post(BACKEND_URL, json={"query": prompt}, timeout=30)
                response.raise_for_status()

                result = response.json()
                # The backend returns {"response": dict}, so we need to format it
                if "response" in result:
                    # Format the response dict nicely
                    if isinstance(result["response"], dict):
                        # Pretty print the dict
                        assistant_response = json.dumps(result["response"], indent=2)
                    else:
                        assistant_response = str(result["response"])
                else:
                    assistant_response = "No response received"

                st.markdown(assistant_response)
                # Add assistant response to chat history
                st.session_state.messages.append({"role": "assistant", "content": assistant_response})

            except requests.exceptions.RequestException as e:
                error_msg = f"Error communicating with backend: {str(e)}"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})
            except json.JSONDecodeError:
                error_msg = "Error parsing response from backend"
                st.error(error_msg)
                st.session_state.messages.append({"role": "assistant", "content": error_msg})

