import streamlit as st
import service as serv
import logIn as login

serv.load_session_state_from_json()

# if 'spotify_access_token' in cookies and cookies['spotify_access_token']:
#     st.session_state.isLogged = True
#     st.session_state.spotify_access_token = cookies['spotify_access_token']

if not st.session_state.isLogged:
    login.login()
else:
    login.display_logged_in()
    st.write(st.session_state.spotify_access_token)
    if st.button('Log out'):
        serv.logout()
        st.experimental_rerun()
