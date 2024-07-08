import streamlit as st
import requests
import uuid
from streamlit_cookies_manager import EncryptedCookieManager
from datetime import datetime, timedelta

def login(cookies):
    state = str(uuid.uuid4())  # Generate a random state value to prevent CSRF attacks
    scope = 'user-read-private user-read-email'
    auth_url = (f"https://accounts.spotify.com/authorize?response_type=code&client_id={st.secrets['CLIENT_ID']}"
                f"&scope={scope}&redirect_uri={st.secrets['REDIRECT_URI']}&state={state}")
    st.session_state.state = state
    st.write(f"Generated state: {st.session_state.state}")  # Debugging log

    st.markdown("<h1 style='text-align: center; color: #1DB954;'>Spotify Login</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Log in to access your Spotify data.</p>", unsafe_allow_html=True)
    
    st.markdown(f"<div style='text-align: center;'><a href='{auth_url}' style='display: inline-block; "
                "padding: 10px 20px; font-size: 18px; color: white; background-color: #1DB954; border-radius: 5px; "
                "text-decoration: none;'>Log in with Spotify</a></div>", unsafe_allow_html=True)
    handle_callback(cookies)

def handle_callback(cookies):
    st.write(st.query_params)

    if 'code' in st.query_params:
        code = st.query_params.code
        received_state = st.query_params.state
        stored_state = st.session_state.state

        st.write(f"Received state: {st.query_params.state}")  # Debugging log
        st.write(f"Stored state: {stored_state}")

        if not stored_state or received_state != stored_state:
            st.error("State mismatch. Please try logging in again.")
            return

        data = {
            'grant_type': 'authorization_code',
            'code': code,
            'redirect_uri': st.secrets['REDIRECT_URI'],
            'client_id': st.secrets['CLIENT_ID'],
            'client_secret': st.secrets['CLIENT_SECRET']
        }

        response = requests.post('https://accounts.spotify.com/api/token', data=data)
        response.raise_for_status()

        token_info = response.json()
        spotify_access_token = token_info.get('spotify_access_token')
        cookies['spotify_access_token'] = spotify_access_token
        cookies.save()

        st.session_state.isLogged = True
        st.session_state.spotify_access_token = spotify_access_token

        st.success("Successfully logged in!")
        st.experimental_rerun()

def display_logged_in():
    st.markdown("<h1 style='text-align: center;'>Welcome!</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>You are logged in with Spotify.</p>", unsafe_allow_html=True)
