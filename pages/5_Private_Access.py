import streamlit as st
from components.header import show_header
from utils.config import PRIVATE_KEY

show_header()

st.header("🔒 Private Access")
st.write(
    "This section is for family/mentors only. Enter the passkey to unlock "
    "the private roadmap and journal."
)

if not st.session_state.get("unlocked"):
    entered = st.text_input("Enter passkey", type="password")
    if entered == PRIVATE_KEY:
        st.session_state["unlocked"] = True
        st.success("🔓 Unlocked! Now navigate to Private Roadmap or Journal.")
        st.rerun() 
    elif entered:
        st.error("❌ Wrong passkey.")
else:
    st.success("🔓 Already unlocked! Use the sidebar to go to Private Roadmap or Journal.")
