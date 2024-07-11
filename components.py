import streamlit as st
import streamlit.components.v1 as components

def title():
    st.markdown("<h1 style='text-align: center; color: #ffffff;'>SpotiFind</h1>", unsafe_allow_html=True)

def slogan():
    st.markdown("<h2 style='text-align: center; color: #1DB954;'>Find your friend circle in music.</h1>", unsafe_allow_html=True)

def landing_animation():
    landing_animation_html = """
        <style>
            .container {
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
        </style>
        <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
        <div class="container">
            <lottie-player 
                src="https://lottie.host/fdc808ce-007b-4b5f-bf83-9873e9615987/RLfdOlZjss.json" 
                background="transparent" 
                speed="0.5" 
                style="width: 400px; height: 400px" 
                loop 
                autoplay 
                direction="1" 
                mode="normal">
            </lottie-player>
        </div>
        """
    components.html(landing_animation_html, height=400)

def logout():
    st.button('Logout')
