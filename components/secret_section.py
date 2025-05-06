import streamlit as st

def show_secret(on_unlocked, correct_key: str) -> None:
    """Render the passkey input and handle unlocking logic."""
    passkey = st.text_input("Enter Passkey", type="password")
    if st.button("Unlock"):
        if passkey == correct_key:
            on_unlocked()
        else:
            st.error("❌ Incorrect passkey. Please try again.")
