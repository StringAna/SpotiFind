import streamlit as st
import requests
from base64 import b64encode
from datetime import datetime, timedelta
import components.user_music as user_music
import components.home_page as home


def login():
    scope = "user-read-private user-read-email"
    auth_url = (
        f"https://accounts.spotify.com/authorize?response_type=code&client_id={st.secrets['CLIENT_ID']}"
        f"&scope={scope}&redirect_uri={st.secrets['REDIRECT_URI']}"
    )

    st.markdown(
        "<h1 style='text-align: center; color: #1DB954;'>Spotify Login</h1>",
        unsafe_allow_html=True,
    )
    st.markdown(
        "<p style='text-align: center;'>Log in to access your Spotify data.</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"<div style='text-align: center;'><a href='{auth_url}' style='display: inline-block; "
        "padding: 10px 20px; font-size: 18px; color: white; background-color: #1DB954; border-radius: 5px; "
        "text-decoration: none;'>Log in with Spotify</a></div>",
        unsafe_allow_html=True,
    )
    handle_callback()


def handle_callback():
    if "code" in st.query_params:
        code = st.query_params["code"]
        access_token = exchange_code_for_token(
            code,
            st.secrets["REDIRECT_URI"],
            st.secrets["CLIENT_ID"],
            st.secrets["CLIENT_SECRET"],
        )

        # Save the access token in session state
        st.session_state.isLogged = True
        st.session_state.spotify_access_token = access_token
        # st.session_state.spotify_refresh_token = refresh_token

        st.success("Successfully logged in!")
        st.rerun()


def exchange_code_for_token(code, redirect_uri, client_id, client_secret):
    auth_header = b64encode(f"{client_id}:{client_secret}".encode()).decode()
    auth_options = {
        "url": "https://accounts.spotify.com/api/token",
        "data": {
            "code": code,
            "redirect_uri": redirect_uri,
            "grant_type": "authorization_code",
        },
        "headers": {
            "Content-Type": "application/x-www-form-urlencoded",
            "Authorization": f"Basic {auth_header}",
        },
    }

    response = requests.post(
        auth_options["url"], data=auth_options["data"], headers=auth_options["headers"]
    )
    response.raise_for_status()

    body = response.json()

    access_token = body["access_token"]

    return access_token


def display_logged_in():
    st.markdown("<h1 style='text-align: center;'>Welcome!</h1>", unsafe_allow_html=True)
    st.markdown(
        "<p style='text-align: center;'>You are logged in with Spotify.</p>",
        unsafe_allow_html=True,
    )
    #user_music.display_user_top_tracks(st.session_state.spotify_access_token)
