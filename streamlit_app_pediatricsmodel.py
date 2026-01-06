import os
import streamlit as st
from openai import OpenAI

# =============================
# 🔑 API KEY VIA ENV VARIABLE
# =============================
# Before running:
#   setx OPENAI_API_KEY "sk-..."
# Then restart your terminal.

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# =============================
# 🌟 Streamlit UI
# =============================
st.set_page_config(page_title="Pediatric Note Summarizer", layout="centered")

st.title("🩺 Pediatric Clinical Note Summarizer")
st.write("This demo uses my fine-tuned pediatric model to summarize clinical notes.")

user_input = st.text_area(
    "Enter a pediatric patient note:",
    placeholder="Example: 6-year-old with fever and cough for 2 days…",
    height=200
)

if st.button("Summarize"):
    if not user_input.strip():
        st.warning("Please enter clinical text.")
    else:
        with st.spinner("Generating summary..."):
            try:
                response = client.chat.completions.create(
                    model="ft:gpt-4o-mini-2024-07-18:personal:peds-notes-v1:CYD9olYs",
                    messages=[
                        {"role": "system", "content": "You are a clinical summarization assistant."},
                        {"role": "user", "content": f"Summarize the following pediatric note:\n\n{user_input}"}
                    ]
                )

                summary = response.choices[0].message.content
                st.success("Summary generated!")
                st.write("---")
                st.subheader("📝 AI-Generated Summary")
                st.write(summary)

            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.stop()
