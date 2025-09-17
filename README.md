
---

# 📊 Excel AI Interviewer

An **AI-powered Excel Interviewer** built using **Streamlit + LangChain + HuggingFace embeddings**.
This project simulates an interactive Excel interview where:

* The interviewer **asks questions via voice** 🗣️
* The candidate **responds through speech** 🎤
* AI evaluates the answer using **semantic similarity** (cosine similarity on embeddings).
* Candidate gets **positive/negative feedback** in real time.
* At the end, a **summary of weak topics** is provided.

---

## 🚀 Features

* 🎙️ **Voice-based interview**: Questions asked via text-to-speech.
* 📝 **Speech-to-text answers**: Candidate replies through microphone.
* 🤖 **AI evaluation**: Semantic similarity check between candidate’s answer and expected answer.
* 💬 **Real-time feedback**: Positive/negative interviewer-style responses.
* 📌 **Summary at the end**: Topics needing improvement are highlighted.
* 🌐 **Deployable on Streamlit Cloud** (publicly shareable).

---

## 🛠️ Tech Stack

* [Streamlit](https://streamlit.io/) – Interactive UI
* [LangChain](https://www.langchain.com/) – Embedding management
* [HuggingFace Transformers](https://huggingface.co/) – Sentence embeddings
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) – Speech-to-text
* [gTTS](https://pypi.org/project/gTTS/) – Text-to-speech
* [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.pairwise.cosine_similarity.html) – Cosine similarity

---

## 📂 Project Structure

```
excel_ai_interviewer/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
└── README.md              # Documentation (this file)
```

---

## ⚙️ Installation (Run Locally)

1. **Clone the repository**

   ```bash
   git clone https://github.com/KHITOLIA/Ai_interviewer.git
   cd excel-ai-interviewer
   ```

2. **Create virtual environment (recommended)**

   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate      # (Windows)
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   streamlit run app.py
   ```

---

## 🎤 Usage

1. Start the app → It will **speak the first Excel question**.
2. Answer verbally (mic required).
3. AI will **transcribe your answer, compare, and give feedback**.
4. Continue until all questions are answered.
5. At the end, you will see a **summary of weak areas**.

---

## ☁️ Deployment (Streamlit Cloud)

1. Push your code to a **GitHub repo**.

   ```
   app.py
   requirements.txt
   README.md
   ```

2. Go to [Streamlit Cloud](https://share.streamlit.io) → **New app**.

3. Select:

   * Repo: `https://github.com/KHITOLIA/Ai_Interviewer`
   * Branch: `main` (or whichever branch you uploaded to)
   * File: `app.py`

4. Click **Deploy** 🚀

5. After a few minutes, your app will be live at:

   ```
https://ai-intervieweer.streamlit.app/
   ```

---

## 🔮 Future Enhancements

* Add more Excel-related questions dynamically from a database.
* Support for **multi-language interviews**.
* Add **leaderboard** for multiple candidates.
* Integration with **OpenAI / Mistral LLMs** for more flexible evaluation.

---

## 👨‍💻 Author

**Your Name**
🔗 GitHub: [KHITOLIA](https://github.com/KHITOLIA)

---
