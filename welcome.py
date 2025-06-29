import streamlit as st

st.set_page_config(page_title="Fluid Mechanics Interactive Tools", layout="wide")

st.markdown("<h1 style='text-align: center;'>Fluid Mechanics Interactive Learning Hub</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; font-weight: normal;'>Welcome! Select a tool below to begin exploring concepts interactively.</h4>", unsafe_allow_html=True)
st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)

st.subheader("Interactive Tools")
st.page_link("pages/capillary_rise.py", label="Capillary Rise Calculator", icon="💧")
st.page_link("pages/hydrostatic_force.py", label="Hydrostatic Force on a Wall", icon="🌊")

st.markdown("---")
st.markdown("""
**Instructions:**
- Click a tool above to begin.
- Use sliders and inputs on each page to see real-time results and diagrams.
""")