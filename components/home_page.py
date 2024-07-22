import streamlit as st
import requests
import webbrowser
from urllib.parse import urlencode
from streamlit_navigation_bar import st_navbar
import components.service as serv


def display_navbar():
    pages = ["Home", "Profile", "Find Friends", "Logout"]
    page = st.sidebar.selectbox("Navigate", pages)
    return page


def display_home():
    st.write("Welcome to the Home Page!")


def display_profile():
    user_info = serv.fetch_user_info()
    st.write("Profile Page")
    st.json(user_info)  # Example of displaying user info


def display_find_friends():
    st.write("Find Friends Page")


def handle_page_navigation():
    page = display_navbar()

    if page == "Home":
        display_home()
    elif page == "Profile":
        display_profile()
    elif page == "Find Friends":
        display_find_friends()
    elif page == "Logout":
        # serv.handle_logout(cookie_manager)
        # st.experimental_rerun()
        st.write("Logout Page")
