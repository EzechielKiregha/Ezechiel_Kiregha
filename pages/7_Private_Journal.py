import streamlit as st
from components.header import show_header

show_header()

st.header("🔒 Private Journal")
st.write("This is the private journal section, accessible only with the correct passkey.")

# Example journal entries
st.subheader("Journal Entry 1")
st.write("Today, I made significant progress on the Hydrogen project...")

st.subheader("Journal Entry 2")
st.write("Explored new opportunities for expanding the Carbon marketplace...")
