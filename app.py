import streamlit as st
from google import genai

# Replace with your NEW Gemini API key (only for testing)
API_KEY = "AQ.Ab8RN6L2eTe1Db-3oMeS8XHzCP162JbcE7BWmlpYiRVuXbPhOg"

client = genai.Client(api_key=API_KEY)

st.set_page_config(
    page_title="AI Learning Buddy",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Learning Buddy")
st.write("Learn any topic with the help of Gemini AI!")

topic = st.text_input("Enter a topic or ask a question")

option = st.selectbox(
    "Choose an option",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Summarize Topic",
        "Ask Anything"
    ]
)

if st.button("Generate"):

    if not topic.strip():
        st.warning("Please enter a topic.")

    else:

        if option == "Explain Concept":
            prompt = f"Explain '{topic}' in simple language for a beginner."

        elif option == "Real-Life Example":
            prompt = f"Give a real-life example of '{topic}'."

        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions on '{topic}' with answers."

        elif option == "Summarize Topic":
            prompt = f"Summarize '{topic}' in bullet points."

        else:
            prompt = topic

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.subheader("🤖 AI Response")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
