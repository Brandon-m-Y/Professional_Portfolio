import streamlit as st

# ====================== PAGE CONFIG ======================
st.set_page_config(
    page_title="Brandon Ytuarte | Analytics Portfolio",
    page_icon="images/BMY_Logo_cropped_2.jpg",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ====================== LOGO ======================
st.logo("images/BMY_Logo_cropped 2.jpg")

# ====================== DEFINE PAGES ======================
# Create StreamlitPage objects once
home_page = st.Page("0_Home_Page.py", title="Home", icon="🏠")
capstone_page = st.Page("1_MSBA_Capstone_Project.py", title="MSBA Capstone", icon="📊")
segmentation_page = st.Page("2_Marketing_Segmentation_App.py", title="Marketing Segmentation", icon="🎯")
credit_page = st.Page("3_Credit _Risk_Modeling.py", title="Credit Risk ML", icon="📈")
job_page = st.Page("4_Python_Data_Job_Analysis_4.py", title="Data Job Analysis", icon="🔬")

# ====================== SIDEBAR NAVIGATION ======================
st.sidebar.title("Featured Projects:")
st.sidebar.write("Click on a project below to get started!")

# Custom sidebar links using the same Page objects (this fixes the KeyError)
st.sidebar.page_link(home_page, label="Home")
st.sidebar.page_link(capstone_page, label="MSBA Capstone")
st.sidebar.page_link(segmentation_page, label="Marketing Segmentation")
st.sidebar.page_link(credit_page, label="Credit Risk ML")
st.sidebar.page_link(job_page, label="Data Job Analysis")

# ====================== HIDDEN NAVIGATION FOR ROUTING ======================
pg = st.navigation(
    [home_page, capstone_page, segmentation_page, credit_page, job_page],
    position="hidden"   # Hides the automatic navigation
)

pg.run()