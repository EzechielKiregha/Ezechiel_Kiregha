import streamlit as st

def show_secret(on_unlocked, correct_key: str):
    """Renders a password box, and if correct sets session_state['unlocked']=True and calls on_unlocked()."""
    entered = st.text_input("Enter passkey", type="password")
    if entered:
        if entered == correct_key:
            st.session_state["unlocked"] = True
            on_unlocked()
        else:
            st.error("❌ Wrong passkey.")
