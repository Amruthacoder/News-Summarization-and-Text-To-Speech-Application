# 📰 News Sentiment Analysis with Hindi TTS 🎙️

![Alt](https://static-blog.onlyoffice.com/wp-content/uploads/2023/08/14123647/ONLYOFFICE-10-text-to-speech-tools-to-consider-in-2023.png)


## 📌 Project Overview

This project scrapes news articles, summarizes them using NLP models, performs sentiment analysis, and generates Hindi text-to-speech (TTS) audio.

## ✅ Features:
	•	Web scraping of news articles
	•	AI-powered summarization using BART
	•	Sentiment analysis with TextBlob
	•	Hindi Text-to-Speech (TTS) using gTTS
	•	Interactive Streamlit Web App

⸻

⚡ How It Works
	1.	User selects a company (Apple/Samsung)
	2.	News articles are scraped from multiple sources
	3.	Summarization & sentiment analysis is performed
	4.	Hindi TTS audio is generated for sentiment summary
	5.	Users can view sentiment reports and play audio

⸻

## 🚀 Deployment & Setup

🛠️ Local Setup (Run on Your Machine)

1️⃣ Clone the Repository

git clone https://github.com/Amruthacoder/Amruthacoder-News-Summarization-and-Text-to-Speech-Application.git
cd Amruthacoder-News-Summarization-and-Text-to-Speech-Application

2️⃣ Create a Virtual Environment & Install Dependencies

python -m venv venv
source venv/bin/activate   # On Mac/Linux
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

3️⃣ Run FastAPI Backend

uvicorn api:app --host 0.0.0.0 --port 8000

FastAPI will be live at: http://127.0.0.1:8000

4️⃣ Run Streamlit App

In a new terminal window, run:

streamlit run app.py

Streamlit app will be available at http://localhost:8501

⸻

## 🌍 Deployed Versions

🔹 FastAPI Backend on Render

👉 [Live API on Render]()

🔹 Streamlit App on Hugging Face

👉 [Live App on Hugging Face]() 

⸻

## 📁 Project Structure

📂 News-Summarization-Hindi-TTS
│── 📄 app.py               # Streamlit frontend
│── 📄 api.py               # FastAPI backend
│── 📄 utils.py             # Helper functions (scraping, analysis, TTS)
│── 📄 requirements.txt      # Project dependencies
│── 📄 README.md             # Project documentation


⸻

## 📝 Tech Stack & Libraries
	•	Python
	•	FastAPI – Backend API
	•	Streamlit – Frontend UI
	•	BeautifulSoup – Web Scraping
	•	Hugging Face Transformers (BART) – Summarization
	•	TextBlob – Sentiment Analysis
	•	YAKE – Keyword Extraction
	•	gTTS – Hindi Text-to-Speech

⸻

## 📌 Future Enhancements

🔹 Support for more languages in TTS
🔹 Add more news sources for better coverage
🔹 Optimize sentiment analysis models

⸻

📧 Contact & Contributions

🙋‍♀️ Created by: Amrutha Yenikonda
📩 Email: amruthayenikonda@gmail.com

⸻

⭐ If you found this project useful, give it a star on GitHub! 🌟
