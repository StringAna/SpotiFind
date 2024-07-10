import streamlit as st
import service as serv


####################################################
# Streamlit App
####################################################

st.title('Spotify Auth with Streamlit')

cookie_manager = serv.initialize_session()
query_params = serv.get_query_params()

access_token = cookie_manager.get('spotify_access_token')
refresh_token = cookie_manager.get('spotify_refresh_token')

if access_token:
    st.session_state['access_token'] = access_token
    st.session_state['refresh_token'] = refresh_token
    st.session_state['isLogged'] = True

if not st.session_state['isLogged']:
    serv.handle_login(cookie_manager)
    serv.handle_callback(cookie_manager, query_params)
       
else:
    serv.fetch_user_info()

    # if st.button('Refresh Token'):
    #     serv.handle_token_refresh(cookie_manager)

    if st.button('Logout'):
        serv.handle_logout(cookie_manager)

