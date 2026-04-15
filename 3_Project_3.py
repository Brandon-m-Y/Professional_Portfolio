import streamlit as st


st.title('This Page Will Be for Project 3')
st.divider()

st.header("More details on this project to come. Until then..")

if st.button("Click Me for Balloons!"):
    st.success('Woohoo')
    st.balloons()
