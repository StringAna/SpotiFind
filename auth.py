import requests
import extra_streamlit_components as stx
from urllib.parse import urlencode
import base64
import streamlit as st


CLIENT_ID = st.secrets.CLIENT_ID
CLIENT_SECRET = st.secrets.CLIENT_SECRET
REDIRECT_URI = 'http://localhost:8501'

cookie_manager = stx.CookieManager()

def generate_random_string(length):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def get_auth_url(state):
    scope = 'user-read-private user-read-email'
    auth_url = 'https://accounts.spotify.com/authorize?' + urlencode({
        'response_type': 'code',
        'client_id': CLIENT_ID,
        'scope': scope,
        'redirect_uri': REDIRECT_URI,
        'state': state
    })
    return auth_url

def get_token(code):
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'authorization_code',
        'code': code,
        'redirect_uri': REDIRECT_URI
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()

def refresh_token(refresh_token):
    url = 'https://accounts.spotify.com/api/token'
    headers = {
        'Authorization': 'Basic ' + base64.b64encode((CLIENT_ID + ':' + CLIENT_SECRET).encode()).decode(),
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    data = {
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json()
