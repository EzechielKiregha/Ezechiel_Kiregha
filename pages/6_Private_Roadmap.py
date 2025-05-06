import streamlit as st
from components.header import show_header
from utils.data import roadmap

show_header()

st.header("🔒 Private Roadmap")
st.write("This is the private roadmap section, accessible only with the correct passkey.")

# Render the private roadmap table
for event in roadmap:
    st.markdown(f"- **{event['phase']}**: {event['milestone']} ({event['status']})")
