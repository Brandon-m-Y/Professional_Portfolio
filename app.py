import streamlit as st

pg = st.navigation([st.Page("0_Home_Page.py"),
                    st.Page("1_MSBA_Capstone_Project.py"), 
                    st.Page("2_Marketing_Segmentation_App.py"),
                    st.Page("3_Project_3.py"),
                    st.Page("4_Project_4.py")])

st.page_icon="images\BMY_Logo_cropped 2.jpg"
st.logo("images\BMY_Logo_cropped 2.jpg")

pg.run()