import streamlit as st
from components.header import show_header
from utils.data import about_metrics

show_header()   # Optional: your reusable header with name & tagline

st.header("👨‍💻 About Me")
st.write("""
I empower Congolese and African youth through elemental‑themed tech services—
from foundational e‑learning to entrepreneurial accelerators.
""")

# Display your top‑line metrics
cols = st.columns(len(about_metrics))
for col, metric in zip(cols, about_metrics):
    with col:
        st.metric(label=metric["label"], value=metric["value"], delta=metric.get("delta"))
