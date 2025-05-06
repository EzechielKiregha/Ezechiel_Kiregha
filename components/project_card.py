import streamlit as st

def project_card(title: str, desc: str, link: str, metrics: dict = None):
    """
    Renders a project “card” with optional metrics.
    
    Args:
      title: Project title
      desc: Short description
      link: URL or “#”
      metrics: Optional dict of { label: value } to show beneath description
    """
    # start card container
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    
    # title & description
    st.markdown(f"### {title}")
    st.markdown(f"<p>{desc}</p>", unsafe_allow_html=True)
    
    # metrics row (if any)
    if metrics:
        cols = st.columns(len(metrics))
        for (label, value), col in zip(metrics.items(), cols):
            with col:
                st.metric(label=label, value=value)
    
    # link button
    st.markdown(f"[🔗 View Project]({link})", unsafe_allow_html=True)
    
    # end card container
    st.markdown("</div>", unsafe_allow_html=True)
