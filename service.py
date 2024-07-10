import streamlit as st
import json

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

def logout(cookie_manager):
    st.session_state.isLogged = False
    st.session_state.access_token = None
    st.session_state.refresh_token = None
    if cookie_manager.get('spotify_auth_state'):
        cookie_manager.delete('spotify_auth_state')
        st.rerun()
