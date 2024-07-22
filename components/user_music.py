# user_music.py
import streamlit as st
import requests


def display_user_top_tracks(access_token):
    # Spotify Web API endpoint for getting recommendations
    url = "https://api.spotify.com/v1/recommendations"
    # Example parameters for recommendations
    params = {"seed_genres": "pop", "limit": 10}
    headers = {"Authorization": f"Bearer {access_token}"}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        recommendations = response.json()
        # Process and display recommendations
        for track in recommendations["tracks"]:
            print(track["name"], "-", track["artists"][0]["name"])
    else:
        print("Failed to fetch recommendations:", response.text)
