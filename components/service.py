import streamlit as st
import json
import requests
import auth
import extra_streamlit_components as stx


def load_session_state_from_json(file_path="state.json"):
    try:
        with open(file_path, "r") as f:
            session_data = json.load(f)
        for key, value in session_data.items():
            if key not in st.session_state:
                st.session_state[key] = value
    except FileNotFoundError:
        st.write("No session state file found. Starting with empty session state.")
    except json.JSONDecodeError:
        st.write("Error reading session state file. Starting with empty session state.")


def initialize_session():
    """Initialize session state and cookie manager."""
    load_session_state_from_json()
    st.session_state.setdefault("isLogged", False)
    st.session_state.setdefault("access_token", None)
    st.session_state.setdefault("refresh_token", None)
    st.session_state.setdefault("is_Log_in_clicked", None)
    return stx.CookieManager()


def get_query_params():
    """Fetch query parameters from the URL."""
    return st.query_params


def handle_login(cookie_manager):
    """Handle the login process and redirection to Spotify auth."""
    login_button = st.button("Login with Spotify")
    if login_button:
        state = auth.generate_random_string(16)
        cookie_manager.set("spotify_auth_state", state)
        auth_url = auth.get_auth_url(state)
        st.query_params  # Clear query params
        st.markdown(
            f'<meta http-equiv="refresh" content="0; url={auth_url}">',
            unsafe_allow_html=True,
        )


def handle_callback(cookie_manager, query_params):
    """Handle the callback from Spotify with authorization code."""
    code = query_params.get("code", [None])
    state = query_params.get("state", [None])
    stored_state = cookie_manager.get("spotify_auth_state")

    if code and state and stored_state and state == stored_state:
        token_info = auth.get_token(code)
        if "access_token" in token_info:
            st.session_state["access_token"] = token_info["access_token"]
            st.session_state["refresh_token"] = token_info["refresh_token"]
            cookie_manager.set("spotify_access_token", token_info["access_token"])
            cookie_manager.set("spotify_refresh_token", token_info["refresh_token"])
            st.session_state["isLogged"] = True
            st.query_params  # Clear query params
        # else:
        #     st.error("Failed to get access token")
    elif state != stored_state:
        st.error("State mismatch")


def fetch_user_info():
    """Fetch and display user information from Spotify."""
    # headers = {"Authorization": f'Bearer {st.session_state["access_token"]}'}
    # user_info = requests.get("https://api.spotify.com/v1/me", headers=headers).json()
    # st.write(user_info)
    headers = {"Authorization": "Bearer YOUR_ACCESS_TOKEN"}
    response = requests.get("https://api.spotify.com/v1/me", headers=headers)

    # Check if the response's status code indicates success
    if response.status_code == 200:
        # Ensure the content type of the response is JSON before parsing
        if "application/json" in response.headers.get("Content-Type"):
            user_info = response.json()
            return user_info
        else:
            print("Response content is not in JSON format.")
            return None
    else:
        print(f"Failed to fetch user info. Status code: {response.status_code}")
        # Optionally, log or print the response text to understand the error better
        print("Response:", response.text)
        return None


def handle_token_refresh(cookie_manager):
    """Handle token refresh and update session state and cookies."""
    token_info = auth.refresh_token(st.session_state["refresh_token"])
    if "access_token" in token_info:
        st.session_state["access_token"] = token_info["access_token"]
        st.session_state["refresh_token"] = token_info.get(
            "refresh_token", st.session_state["refresh_token"]
        )
        cookie_manager.set("spotify_access_token", token_info["access_token"])
        cookie_manager.set("spotify_refresh_token", token_info["refresh_token"])
    else:
        st.error("Failed to refresh token")


def handle_logout(cookie_manager):
    """Handle user logout and clear session state and cookies."""
    cookie_manager.delete("spotify_access_token")
    cookie_manager.delete("spotify_refresh_token")
    cookie_manager.delete("spotify_auth_state")
    st.session_state.clear()
    st.set_query_params  # Clear query params
    st.rerun()
