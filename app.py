import streamlit as st
import numpy as np
import random
import time
import tempfile
from sklearn.metrics.pairwise import cosine_similarity
from langchain_huggingface.embeddings import HuggingFaceEmbeddings
from gtts import gTTS
from st_audiorec import st_audiorec
import speech_recognition as sr

# Load Embedding Model
model_name = 'sentence-transformers/all-mpnet-base-v2'
embedding_model = HuggingFaceEmbeddings(model_name=model_name)

# Positive & Negative Responses
positive_response = [
    "That’s a good answer, you explained it well.",
    "Correct, your response is relevant to the question.",
    "Good point, that’s exactly what I was expecting.",
    "Yes, that’s the right direction.",
    "Your explanation makes sense, let’s move ahead.",
]

negative_response = [
    "I appreciate your effort, but that doesn’t fully address the question.",
    "That’s an interesting perspective, though it’s not exactly what I was looking for.",
    "Good attempt, but your answer is slightly off.",
    "You’re on the right track, but something important is missing.",
    "Thanks for sharing, though it doesn’t quite match the question.",
]

# Excel Q&A
excel_qna = {
    "How do you remove duplicate values from a column in Excel?": {
        "answer": "Select the column > Data tab > Remove Duplicates.",
        "topic": "Data Cleaning"
    },
    "What does VLOOKUP do in Excel?": {
        "answer": "VLOOKUP searches for a value in the first column of a range and returns a value in the same row from another column.",
        "topic": "Lookup & Reference"
    }
}

# --- Typing Effect ---
def typing_effect(text, speed=0.05):
    placeholder = st.empty()
    typed_text = ""
    for char in text:
        typed_text += char
        placeholder.markdown(f"🧑🏻‍💼 **Interviewer:** {typed_text}")
        time.sleep(speed)

# --- Text to Speech ---
def speak_text(text, filename="voice.mp3"):
    tts = gTTS(text)
    tts.save(filename)
    st.audio(filename, format="audio/mp3", autoplay=True)

# --- Speech to Text ---
def audio_to_text(audio_bytes):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmpfile:
        tmpfile.write(audio_bytes)
        tmpfile.flush()
        recognizer = sr.Recognizer()
        with sr.AudioFile(tmpfile.name) as source:
            audio = recognizer.record(source)
        try:
            return recognizer.recognize_google(audio)
        except:
            return None
        

        # --- Session State Initialization ---
if "current_question" not in st.session_state:
    st.session_state.current_question = list(excel_qna.keys())[0]
    st.session_state.asked = []
    st.session_state.summary = []

# 👇 ALWAYS initialize the flag (even if already in session_state)
if "question_spoken" not in st.session_state:
    st.session_state.question_spoken = False

# --- Session State ---
if "current_question" not in st.session_state:
    st.session_state.current_question = list(excel_qna.keys())[0]
    st.session_state.asked = []
    st.session_state.summary = []
    st.session_state.question_spoken = False   # 👈 new flag

question = st.session_state.current_question

if question:
    answer = excel_qna[question]["answer"]
    topic = excel_qna[question]["topic"]

    # Ask question only once
    if not st.session_state.question_spoken:
        typing_effect(question)
        speak_text(question)
        st.session_state.question_spoken = True   # 👈 prevent repeat

    st.write("🎙️ Record your answer below:")
    audio_bytes = st_audiorec()

    if audio_bytes is not None:
        st.audio(audio_bytes, format="audio/wav")

        if st.button("Submit Answer"):
            user_input = audio_to_text(audio_bytes)

            if user_input:
                st.write(f"🗣️ Candidate: {user_input}")

                # Embedding similarity
                user_embedding = embedding_model.embed_query(user_input)
                answer_embedding = embedding_model.embed_query(answer)
                similarity = cosine_similarity([user_embedding], [answer_embedding])[0][0] * 100

                if similarity > 80:
                    response = random.choice(positive_response)
                    st.success(f"✅ Interviewer: {response}")
                    speak_text(response)
                    st.write(f"**Your Score:** {int(np.round(similarity))}")
                else:
                    response = random.choice(negative_response)
                    st.error(f"❌ Interviewer: {response}")
                    speak_text(response)
                    st.session_state.summary.append(topic)

                # Move to next question
                st.session_state.asked.append(question)
                remaining = [q for q in excel_qna.keys() if q not in st.session_state.asked]

                if remaining:
                    st.session_state.current_question = remaining[0]
                else:
                    st.session_state.current_question = None

                st.session_state.question_spoken = False  # 👈 reset for next Q
                st.rerun()   # force rerun to load next Q immediately
            else:
                st.warning("⚠️ Could not recognize your speech. Try again.")

# --- Summary ---
if st.session_state.current_question is None:
    st.subheader("📌 Interview Summary")
    if st.session_state.summary:
        st.error("You should focus more on these topics:")
        for t in set(st.session_state.summary):
            st.write(f"- {t}")
    else:
        st.success("🎉 Great job! You performed well in all topics.")
