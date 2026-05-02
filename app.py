import streamlit as st
from scam_detector import detect_scam

st.title("Online Scam Detection System")

user_input = st.text_area("Enter message, email, or link:")

if st.button("Check"):
    result = detect_scam(user_input)
    st.success(result)