import streamlit as st
from components.header import show_header
from utils.data import projects_list
from components.project_card import project_card


show_header()

st.header("🚀 Projects")

# projects_list should be a list of dicts with title, description, link, and optional metrics
for p in projects_list:
    project_card(
        title=p["title"],
        desc=p["description"],
        link=p["link"],
        metrics=p.get("metrics", {})
    )
