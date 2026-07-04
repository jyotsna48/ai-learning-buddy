import streamlit as st
from google import genai

API_KEY = "AQ.Ab8RN6L2eTe1Db-3oMeS8XHzCP162JbcE7BWmlpYiRVuXbPhOg"

st.title("Gemini Test")

try:
    client = genai.Client(api_key=API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents="Say Hello"
    )

    st.success(response.text)

except Exception as e:
    st.error(str(e))
