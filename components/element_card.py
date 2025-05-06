import streamlit as st

def element_card(e: dict):
    """
    Renders an “element” mini‑case study card.
    Expects keys: symbol, name, problem, solution, impact, next
    """
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # Element header
    st.markdown(f"## {e['symbol']} – {e['name']}")
    
    # Problem → Solution → Impact → Next
    st.markdown(f"**Problem:** {e['problem']}")
    st.markdown(f"**Solution:** {e['solution']}")
    st.markdown(f"**Impact:** {e['impact']}")
    st.markdown(f"**Next:** {e['next']}")
    
    st.markdown("</div>", unsafe_allow_html=True)
