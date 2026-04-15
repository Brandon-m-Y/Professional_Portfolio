import streamlit as st
from pathlib import Path

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Brandon Ytuarte | Analytics Portfolio",
    page_icon="images//BMY_Logo_cropped_2.jpg",   # This becomes your browser favicon
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== LOGO ======================
# Use forward slashes + recommended filename without spaces
st.logo("images/BMY_Logo_cropped 2.jpg")   # This shows in the top-left of the app

# ====================== NAVIGATION ======================
pg = st.navigation([
    st.Page("0_Home_Page.py", title="Home", icon="🏠"),
    st.Page("1_MSBA_Capstone_Project.py", title="MSBA Capstone", icon="📊"),
    st.Page("2_Marketing_Segmentation_App.py", title="Marketing Segmentation", icon="🎯"),
    st.Page("3_Project_3.py", title="Project 3", icon="📈"),
    st.Page("4_Project_4.py", title="Project 4", icon="🔬")
])

pg.run()