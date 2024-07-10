import streamlit as st
import requests
import auth
import extra_streamlit_components as stx
import service

st.title('Spotify Auth with Streamlit')

service.load_session_state_from_json()

cookie_manager = stx.CookieManager()

query_params = st.query_params
state = query_params.get('state', [None])
code = query_params.get('code', [None])

# Check if the user is logged in by checking the cookie
access_token = cookie_manager.get('spotify_access_token')
refresh_token = cookie_manager.get('spotify_refresh_token')

if access_token:
    st.session_state['access_token'] = access_token
    st.session_state['refresh_token'] = refresh_token
    st.session_state['is_logged_in'] = True

if not st.session_state.get('is_logged_in', False):
    login_button = st.button('Login with Spotify')
    if login_button:
        state = auth.generate_random_string(16)
        st.write(f'Generated state: {state}')  # Debugging statement
        cookie_manager.set('spotify_auth_state', state)
        st.write(f'Stored state: {cookie_manager.get("spotify_auth_state")}')  # Debugging statement
        auth_url = auth.get_auth_url(state)
        st.query_params
        st.markdown(f'<meta http-equiv="refresh" content="0; url={auth_url}">', unsafe_allow_html=True)

    if code:
        stored_state = cookie_manager.get('spotify_auth_state')
        st.write(f'State: {state}, Stored State: {stored_state}')  # Debugging statement
        if state and stored_state and state == stored_state:
            token_info = auth.get_token(code)
            if 'access_token' in token_info:
                st.session_state['access_token'] = token_info['access_token']
                st.session_state['refresh_token'] = token_info['refresh_token']
                cookie_manager.set('spotify_access_token', token_info['access_token'])
                cookie_manager.set('spotify_refresh_token', token_info['refresh_token'])
                st.session_state['is_logged_in'] = True
                st.query_params
            else:
                st.error("Failed to get access token")
        else:
            st.error("State mismatch")

else:
    headers = {'Authorization': 'Bearer ' + st.session_state['access_token']}
    user_info = requests.get('https://api.spotify.com/v1/me', headers=headers).json()
    st.write(user_info)

    if st.button('Refresh Token'):
        token_info = auth.refresh_token(st.session_state['refresh_token'])
        if 'access_token' in token_info:
            st.session_state['access_token'] = token_info['access_token']
            st.session_state['refresh_token'] = token_info.get('refresh_token', st.session_state['refresh_token'])
            cookie_manager.set('spotify_access_token', token_info['access_token'])
            cookie_manager.set('spotify_refresh_token', token_info['refresh_token'])
        else:
            st.error("Failed to refresh token")

    if st.button('Logout'):
        cookie_manager.delete('spotify_access_token')
        cookie_manager.delete('spotify_refresh_token')
        cookie_manager.delete('spotify_auth_state')
        st.session_state.clear()
        st.rerun()
# else:
#     st.write("Please log in to access your Spotify account.")
