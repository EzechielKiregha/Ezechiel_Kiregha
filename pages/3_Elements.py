# pages/3_Elements.py

import streamlit as st
from components.header import show_header
from components.element_card import element_card
from utils.data import elements

# render sidebar + page header
show_header()

st.header("🧪 Elemental Case Studies")
st.write("Each element is a mini‑case: Problem → Solution → Impact → Next Steps")

# Option A: full‑width list
for e in elements:
    element_card(e)

# Option B: grid with two columns
# cols = st.columns(2)
# for i, e in enumerate(elements):
#     with cols[i % 2]:
#         element_card(e)
