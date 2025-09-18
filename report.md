
---

## 2. report.md  

```markdown
# AI Engineer Assignment – Approach Report

## Problem Understanding
The goal was to build a system that:
- Asks Excel-related interview questions
- Collects candidate answers in text
- Evaluates correctness automatically
- Provides voice + text feedback
- Summarizes performance with a final score

## Solution Design

### 1. User Access
- Implemented **Login & Registration** using JSON storage for simplicity.
- Each candidate session is isolated.

### 2. Question Bank
- A dictionary of Excel Q&A with topics (e.g., Data Cleaning, Lookup & Reference).
- Tracks which questions have been asked and candidate progress.

### 3. Embedding & Evaluation
- Used HuggingFace’s **`all-MiniLM-L6-v2`** for generating semantic embeddings.  
- Computed **cosine similarity** between candidate’s answer and reference answer.
- If similarity ≥ 80% → treated as correct, else incorrect.

### 4. Feedback System
- Maintains **positive** and **negative** response pools.
- Randomly selects a feedback phrase for natural conversation.
- Feedback is shown as text and played as **voice (gTTS)**.

### 5. Interview Flow
- Questions displayed one by one.
- Candidate types an answer and submits.
- AI interviewer evaluates answer, responds with voice + text.
- Moves to next question until all are done.

### 6. Final Scoring
- At the end:
  - Shows correct vs incorrect count
  - Displays weak topics
  - Computes final percentage score
- Redirects back to login page automatically after 10 seconds.

## Tech Stack
- **Streamlit** – UI & flow control
- **HuggingFace MiniLM Embeddings** – semantic vector generation
- **scikit-learn** – cosine similarity computation
- **gTTS** – text-to-speech for interviewer voice
- **JSON file** – user login/registration data store

## Future Improvements
- Add support for **voice input** (speech-to-text answers).
- Expand Excel Q&A dataset.
- Replace JSON with **SQLite/Postgres** for scalable user management.
- Add **analytics dashboard** for candidate performance trends.

