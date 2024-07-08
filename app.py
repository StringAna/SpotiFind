import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager
import service as serv
import logIn as login

cookies = EncryptedCookieManager(prefix="spotify_", password=st.secrets.COOKIES_PASSWORD )

if not cookies.ready():
    st.stop()

serv.load_session_state_from_json()

if 'spotify_access_token' in cookies and cookies['spotify_access_token']:
    st.session_state.isLogged = True
    st.session_state.spotify_access_token = cookies['spotify_access_token']

if not st.session_state.isLogged:
    login.login(cookies)
else:
    login.display_logged_in()
    if st.button('Log out'):
        serv.logout(cookies)
        st.experimental_rerun()
