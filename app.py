import streamlit as st
import requests

# 🎯 Backend API Base URL (Change this to your Render URL)
BASE_URL = "https://news-summarization-and-text-to-speech.onrender.com"

st.title("📰 News Sentiment Analysis with Hindi TTS 🎙️")

# ✅ User selects a company
company = st.selectbox("Choose a company:", ["apple", "samsung"])

if st.button("Fetch News & Sentiment Analysis"):
    with st.spinner("Fetching and analyzing news..."):
        scrape_response = requests.get(f"{BASE_URL}/scrape_news/{company}")

    if scrape_response.status_code == 200:
        st.success(f"✅ News for {company.capitalize()} scraped successfully!")

        news_response = requests.get(f"{BASE_URL}/get_news/{company}")
        if news_response.status_code == 200:
            sentiment_data = news_response.json()

            st.subheader(f"📊 Sentiment Analysis for {company.capitalize()}")
            st.json(sentiment_data)

        else:
            st.error("❌ Error fetching sentiment data.")

    else:
        st.error("❌ Error scraping news.")

# 🎵 **Play Hindi Sentiment Audio**
if st.button("Play Hindi Sentiment Audio 🎵"):
    with st.spinner("Generating TTS..."):
        tts_response = requests.get(f"{BASE_URL}/get_tts/{company}")

    if tts_response.status_code == 200:
        st.success(f"🎙️ Playing Hindi sentiment analysis for {company.capitalize()}...")
        st.audio(f"{BASE_URL}/get_tts/{company}", format="audio/mpeg")
    else:
        st.error("❌ Error fetching Hindi TTS audio.")

# 📂 **Download CSV File**
st.write("### 📂 Download CSV Report")
st.markdown(f"[Download CSV]( {BASE_URL}/get_csv/{company} )")