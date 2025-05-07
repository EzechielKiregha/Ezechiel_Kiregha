import streamlit as st
from components.header import show_header

show_header()

if not st.session_state.get("unlocked"):
    st.error("🔒 Locked. Enter passkey on Private Access page.")
    st.stop()


st.header("🔐 Private Journal & Reflections")

st.markdown("""
> **July 15, 2025**  
> I visited a village school in Masina. The single solar panel powered one lightbulb and charged three phones—but no computers. This cemented my offline‑first priority for Hydrogen’s next sprint.

> **August 2, 2025**  
> Drafted the carbon‑credit model for our vocational marketplace—exploring “C‑tokens” for sustainable farming practices. Feels like turning Carbon into real currency.

> **September 10, 2025**  
> Met with Kinshasa Province officials about smart‑grid pilot. They loved the concept—now drafting the resource‑management API spec.

> **October 1, 2025**  
> Late‑night coding session on Silicon bootcamp curriculum. Realized we need soft‑skills modules: teamwork, communication, problem‑solving.
""", unsafe_allow_html=True)
