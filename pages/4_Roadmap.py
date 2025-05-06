# pages/4_Roadmap.py

import streamlit as st
from components.header import show_header
from components.roadmap_chart import roadmap_chart
from utils.data import roadmap

show_header()

st.header("🗺️ Next Moves Roadmap")
st.write("A concise timeline of our upcoming milestones—public view.")

# Render the roadmap table
roadmap_chart(roadmap)
