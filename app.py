import streamlit as st
from streamlit_option_menu import option_menu
import service as serv

# Load session state from file
serv.load_session_state_from_json()


if st.session_state.isLogged:
    st.button("Logout", on_click =serv.logout, use_container_width = True)
    # 3. CSS style definitions
    selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
        icons=['house', 'cloud-upload', "list-task", 'gear'], 
        menu_icon="cast", default_index=0, orientation="horizontal",
        styles={
            "container": {"padding": "0!important", "background-color": "#fafafa"},
            "icon": {"color": "orange", "font-size": "25px"}, 
            "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
            "nav-link-selected": {"background-color": "green"},
        }
    )
    st.write("Selected:", selected3)
else:
    serv.animation()

