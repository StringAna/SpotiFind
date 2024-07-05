import streamlit as st
import json
import requests

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
def logout():
    st.session_state.isLogged = False

#Function to handle Login button click
def login():
    st.session_state.isLogged = True

def animation():
    """
    Renders the lottie animation.
    """
    lottie_json = load_lottieurl("https://lottie.host/ba9ea9cc-2cf2-48f2-bf62-a1fcf7597c85/ldLmo4eDAf.json")
    if lottie_json:
        st.lottie(lottie_json, speed=1, key="animation")
        st.button("Login", on_click=login, use_container_width = True)
    else:
        st.write("Failed to load animation.")

def load_lottieurl(url):
    """
    Fetches the lottie animation using the URL.
    """
    try:
        r = requests.get(url)
        if r.status_code == 200 and 'application/json' in r.headers.get('Content-Type', ''):
            return r.json()
        else:
            st.error(f"Failed to load Lottie URL: {url} with status code: {r.status_code} and Content-Type: {r.headers.get('Content-Type')}")
            return None
    except Exception as e:
        st.error(f"An error occurred while fetching the Lottie URL: {url}. Error: {e}")
        return None