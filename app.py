import streamlit as st
from google import genai

# ✅ Read API key safely from Streamlit Secrets
client = genai.Client(api_key=st.secrets["AQ.Ab8RN6L2eTe1Db-3oMeS8XHzCP162JbcE7BWmlpYiRVuXbPhOg"])
st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓")

st.title("🎓 AI Learning Buddy (Capstone Project)")
st.write("Your smart AI study assistant powered by Gemini 🚀")

# Input
topic = st.text_input("Enter your topic or question")

# Feature selection
option = st.selectbox(
    "Choose what you want",
    [
        "Explain Concept",
        "Real-Life Example",
        "Generate Quiz",
        "Doubt Solver (Chat)",
        "Summarize Topic"
    ]
)

# Button
if st.button("Generate Response"):

    if not topic:
        st.warning("Please enter a topic!")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple beginner-friendly language with examples."

        elif option == "Real-Life Example":
            prompt = f"Give a real-life example of {topic} in simple terms."

        elif option == "Generate Quiz":
            prompt = f"Create 5 multiple-choice questions on {topic} with answers."

        elif option == "Summarize Topic":
            prompt = f"Summarize {topic} in short bullet points."

        else:
            prompt = f"You are a helpful AI tutor. Answer this question clearly: {topic}"

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            st.markdown("### 🤖 AI Response")
            st.write(response.text)

        except Exception as e:
            st.error("Something went wrong. Please check API key or try again.")
            st.code(str(e))
