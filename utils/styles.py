from pathlib import Path
import streamlit as st


def load_css() -> None:
    """Load custom CSS styles for the Streamlit app."""
    css_path = Path(__file__).parent.parent / "static" / "styles.css"
    st.markdown(f"<style>{css_path.read_text()}</style>", unsafe_allow_html=True)
