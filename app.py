import streamlit as st

st.title("AI Learning Buddy 🚀")

st.write("Your Streamlit app is working!")

name = st.text_input("Enter your name")

if name:
    st.success(f"Hello {name} 👋 Welcome to your AI buddy!")
