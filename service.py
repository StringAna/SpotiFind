import streamlit as st
import json
from streamlit_cookies_manager import EncryptedCookieManager

# Function to save session state to a file
def load_session_state_from_json(file_path="state.json"):
    try:
        with open(file_path, 'r') as f:
            session_data = json.load(f)
        for key, value in session_data.items():
            if key not in st.session_state:
                st.session_state[key] = value
    except FileNotFoundError:
        st.write("No session state file found. Starting with empty session state.")
    except json.JSONDecodeError:
        st.write("Error reading session state file. Starting with empty session state.")

# Function to handle Logout button click
def logout(cookies):
    st.session_state.isLogged = False
    st.session_state.access_token = None

    # Remove access_token from cookies
    if 'access_token' in cookies:
        del cookies['access_token']
        cookies.save()
