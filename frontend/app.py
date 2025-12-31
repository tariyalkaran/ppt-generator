
# frontend/app.py
import sys
from pathlib import Path

# Resolve project root: .../OSPAI_PPT_Generator
PROJECT_ROOT = Path(__file__).resolve().parent.parent
# Ensure it's on sys.path (at the front)
sys.path.insert(0, str(PROJECT_ROOT))

import streamlit as st

# (optional) quick debug to confirm:
# st.write("PYTHONPATH:", sys.path)





# app.py
import streamlit as st

st.set_page_config(page_title="AI PPT Generator", layout="wide", page_icon="📊")

st.title("AI PPT Generator")
st.write("This app uses a multi-page flow. Use the sidebar to navigate or click below to start.")
if st.button("Go to Home (Start)"):
    try:
        st.query_params(page="1_Home")
        st.switch_page("pages/1_Home.py")
    except Exception:
        # fallback: Streamlit versions differ; link to the Home page in sidebar
        st.info("Use the sidebar pages to navigate to Home.")
