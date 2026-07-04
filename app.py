import streamlit as st
import google.generativeai as genai

# Replace with your NEW Gemini API key
genai.configure(api_key="AQ.Ab8RN6L2eTe1Db-3oMeS8XHzCP162JbcE7BWmlpYiRVuXbPhOg")

model = genai.GenerativeModel("gemini-1.5-flash")

st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓")

st.title("🎓 AI Learning Buddy")

question = st.text_input("Ask anything")

if st.button("Generate"):
    if question.strip():
        try:
            response = model.generate_content(question)
            st.write(response.text)
        except Exception as e:
            st.error(str(e))
    else:
        st.warning("Please enter a question.")
