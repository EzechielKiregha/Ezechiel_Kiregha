import streamlit as st
from components.header import show_header
from components.secret_section import show_secret
from utils.config import PRIVATE_KEY

show_header()

st.header("🔒 Private Access")
st.write(
    "This section is for family/mentors only. Enter the passkey to unlock "
    "the private roadmap and journal."
)

def on_unlocked() -> None:
    """Callback function to execute when the correct passkey is entered."""
    st.success("🔓 Access granted!")
    st.write("You can now navigate (via the sidebar) to:")
    st.markdown("- **Private Roadmap** (Page 6)\n- **Private Journal** (Page 7)")

# Render the passkey input and unlock logic
show_secret(on_unlocked, correct_key=PRIVATE_KEY)
