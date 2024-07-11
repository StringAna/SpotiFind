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
                position: relative; 
            }
            .animation1 {
                position: absolute;
                z-index: 1;
            }
            .animation2 {
                position: absolute;
                z-index: 2;
            }
        </style>
        <div class="container">
            <div class="animation1">
                <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
                <lottie-player 
                    src="https://lottie.host/d2f88de3-c902-4a33-a28e-5e2ac7c7cdff/hq4c6quVwI.json" 
                    background="transparent" 
                    speed="0.3" 
                    style="width: 80vw; height: 80vh" 
                    loop
                    autoplay 
                    direction="1" 
                    mode="normal">
                </lottie-player>
            </div>
            <div class="animation2">
                <script src="https://unpkg.com/@lottiefiles/lottie-player@latest/dist/lottie-player.js"></script>
                <lottie-player 
                    src="https://lottie.host/bc6a4a8a-ed6e-4691-ad3d-d1eb9009df5d/9VbrP9d1Z5.json" 
                    background="transparent" 
                    speed="0.6" 
                    style="width: 100vw; height: 100vh" 
                    loop 
                    autoplay 
                    direction="1" 
                    mode="normal">
                </lottie-player>
            </div>
        </div>
        """
    components.html(landing_animation_html, height=400)
    
def logout():
    st.button('Logout')
