import streamlit as st
from streamlit_option_menu import option_menu
import service as serv
import logIn as login

# Load session state from file
serv.load_session_state_from_json()


if not st.session_state.isLogged:
    login.login()
    st.session_state.isLogged = True
else:
    login.handle_callback()

