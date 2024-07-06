import streamlit as st
import requests
import uuid
from urllib.parse import parse_qsl

# Streamlit runs on 8501 by default

def login():
    state = str(uuid.uuid4())
    scope = 'user-read-private user-read-email'
    auth_url = (f"https://accounts.spotify.com/authorize?response_type=code&client_id={st.secrets['CLIENT_ID']}"
                f"&scope={scope}&redirect_uri={st.secrets['REDIRECT_URI']}&state={state}")
    st.session_state['state'] = state
    
    # Add some descriptive text
    st.markdown("<h1 style='text-align: center; color: #1DB954;'>Spotify Login</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Log in to access your Spotify data.</p>", unsafe_allow_html=True)
    
    # Center the button
    st.markdown(f"<div style='text-align: center;'><a href='{auth_url}' style='display: inline-block; "
                "padding: 10px 20px; font-size: 18px; color: white; background-color: #1DB954; border-radius: 5px; "
                "text-decoration: none;'>Log in with Spotify</a></div>", unsafe_allow_html=True)

def handle_callback():
    with st.form(key='callback_form'):
        url = st.text_input("Paste the URL you were redirected to here:")
        submit_button = st.form_submit_button(label='Submit')

    if submit_button and url:
        try:
            parsed_url = requests.utils.urlparse(url)
            if not parsed_url.scheme or not parsed_url.netloc:
                st.error("Invalid URL. Please make sure you've copied the full URL.")
                return
            
            query_params = dict(parse_qsl(parsed_url.query))
            if not query_params:
                st.error("No query parameters found in the URL. Please make sure you've copied the full URL including the query parameters.")
                return
            
            code = query_params.get('code')
            state = query_params.get('state')

            # Validate state parameter to prevent CSRF
            if not state or state != st.session_state.get('state'):
                st.error("State mismatch. Please try logging in again.")
                return

            # Prepare the data for the POST request
            data = {
                'grant_type': 'authorization_code',
                'code': code,
                'redirect_uri': st.secrets['REDIRECT_URI'],
                'client_id': st.secrets['CLIENT_ID'],
                'client_secret': st.secrets['CLIENT_SECRET']
            }

            response = requests.post('https://accounts.spotify.com/api/token', data=data)
            response.raise_for_status()  # Raises an HTTPError if the response was an error
            
            st.success("Successfully logged in!")
            token_info = response.json()
            st.write(token_info)

        except Exception as e:
            st.error(f"An error occurred: {e}")

