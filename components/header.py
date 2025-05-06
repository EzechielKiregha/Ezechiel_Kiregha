import streamlit as st

def show_header() -> None:
    """Display the header with name and tagline."""
    # Sidebar header
    st.sidebar.title("🌟 Ezechiel Kiregha")
    st.sidebar.markdown("**Python Developer | Backend Specialist**")
    st.sidebar.markdown("---")
    # custom nav:
    st.sidebar.page_link("Ezechiel_Kiregha.py", label="Home")
    st.sidebar.page_link("pages/1_About.py",     label="About")
    st.sidebar.page_link("pages/2_Projects.py",  label="Projects")
    st.sidebar.page_link("pages/3_Elements.py",  label="Elements")
    st.sidebar.page_link("pages/4_Roadmap.py",     label="Roadmap")
    st.sidebar.markdown("---")
    st.sidebar.page_link("pages/5_Private_Access.py",  label="Private Access")
    st.sidebar.page_link("pages/6_Private_Roadmap.py",  label="Private Roadmap")
    st.sidebar.page_link("pages/7_Private_Journal.py",  label="Private Journal")

