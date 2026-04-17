import streamlit as st

st.title("MSBA Capstone Project")
st.write("This will have some information about the project...")
st.divider()

st.write("More details on this project to come. Until then..")

if st.button("Click Me for Balloons!"):
    st.success('Woohoo')
    st.balloons()


st.write("Each project page includes:" \
" - the business problem, " \
" - technical approach (data science/ML techniques), " \
" - key insights, and " \
" - business value delivered.")