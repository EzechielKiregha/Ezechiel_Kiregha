# This file is part of the Streamlit Components repository.
import streamlit as st

def roadmap_chart(events: list[dict]):
    """
    Renders a concise roadmap as a table.
    Expects each event dict to have: phase, milestone, status.
    """
    # Build markdown table
    md = "| Phase   | Milestone                                          | Status  |\n"
    md += "|---------|----------------------------------------------------|---------|\n"
    for e in events:
        md += f"| {e['phase']} | {e['milestone']} | {e['status']} |\n"
    st.markdown(md)
