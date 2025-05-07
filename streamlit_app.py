import streamlit as st
from components.header import show_header
from utils.styles import load_css

# 1. Page config
st.set_page_config(
    page_title="Ezechiel Kiregha Portfolio",
    page_icon="🌟",
    layout="wide",
    initial_sidebar_state="auto"
)
show_header()  # Optional: your reusable header with name & tagline
# 2. Load global CSS
load_css()


# 3. Welcome
st.title("🌟 Welcome to Ezechiel Kiregha’s Portfolio")
st.image("assets/portfolio.jpeg", use_container_width=True, caption="Ezechiel Kiregha")
st.markdown(
    """
    Welcome to my portfolio! I am a Python Developer and Backend Specialist with a passion for building efficient and scalable applications. 
    My journey has been filled with exciting projects, challenges, and continuous learning.
    """
)
st.markdown(
    """
    This portfolio showcases my journey as a Python Developer and Backend Specialist. 
    It includes my projects, elements of my work, and a roadmap for the future.
    """
)
st.markdown("Use the menu on the left to explore About, Projects, Elements, Roadmap, or—if you have the passkey—Private sections.")
