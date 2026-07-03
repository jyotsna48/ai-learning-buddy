import streamlit as st
from google import genai

# 🔑 Put your Gemini API key here
client = genai.Client(api_key="AQ.Ab8RN6JuzUng6A4Fc5VBVxWOY4JKqOc6ph9lcw_NqBJ0F9qaFQ")

st.set_page_config(page_title="AI Learning Buddy", page_icon="🎓")

st.title("🎓 AI Learning Buddy (Capstone Project)")

st.write("Ask anything and learn with AI!")

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

    if topic == "":
        st.warning("Please enter something!")

    else:

        if option == "Explain Concept":
            prompt = f"Explain {topic} in simple beginner-friendly language."

        elif option == "Real-Life Example":
            prompt = f"Give a real-life example of {topic}."

        elif option == "Generate Quiz":
            prompt = f"Create 5 MCQs on {topic} with answers."

        elif option == "Summarize Topic":
            prompt = f"Summarize {topic} in simple bullet points."

        else:
            prompt = f"You are a helpful AI tutor. Answer this question: {topic}"

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        st.markdown("### 🤖 AI Response")
        st.write(response.text)
