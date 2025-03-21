import os
import requests
import time
import json
import nltk
import yake
from bs4 import BeautifulSoup
from transformers import pipeline
from textblob import TextBlob
from gtts import gTTS

# Download necessary NLTK data
nltk.download("punkt")
nltk.download("stopwords")

# Initialize YAKE and Summarizer
kw_extractor = yake.KeywordExtractor(lan="en", n=2, dedupLim=0.9, top=5)

# ✅ Load once at the start of the script
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

def get_summarizer():
    return pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")  # Lighter model

# ✅ **Scrape Articles**
def scrape_articles(company, urls):
    dir_path = f"data/{company}_articles"
    os.makedirs(dir_path, exist_ok=True)
    output_txt = f"{dir_path}/{company}_articles.txt"

    articles_data = {}

    for idx, url in enumerate(urls, start=1):
        try:
            time.sleep(2)
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")
            title = soup.find("h1").text.strip() if soup.find("h1") else "No title found"
            content = " ".join([p.text.strip() for p in soup.find_all("p")])

            articles_data[idx] = {"title": title, "url": url, "content": content}
            print(f"✅ Scraped: {title}")

        except requests.RequestException as e:
            print(f"❌ Error scraping {url}: {str(e)}")

    # Save articles
    with open(output_txt, 'w', encoding='utf-8') as f:
        for article_number, data in articles_data.items():
            f.write(f"Article Number: {article_number}\n")
            f.write(f"TITLE: {data['title']}\n")
            f.write(f"URL: {data['url']}\n")
            f.write("CONTENT:\n")
            f.write(data['content'])
            f.write("\n" + "=" * 80 + "\n")

    return output_txt

# ✅ **Process Articles (Summarization & Sentiment Analysis)**
def process_articles(company):
    dir_path = f"data/{company}_articles"
    input_txt = f"{dir_path}/{company}_articles.txt"
    output_json = f"{dir_path}/{company}_articles_sentiment.json"

    if not os.path.exists(input_txt):
        return {"error": f"No articles file found for {company}!"}

    with open(input_txt, "r", encoding="utf-8") as f:
        content = f.read()

    articles = content.strip().split("=" * 80)
    data_list = []
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}

    for idx, article in enumerate(articles, start=1):
        lines = article.strip().split("\n")
        if len(lines) < 4:
            continue

        title = lines[1].replace("TITLE: ", "").strip()
        url = lines[2].replace("URL: ", "").strip()
        article_content = "\n".join(lines[4:]).strip()

        summarizer = get_summarizer()  # Load once
        summary = summarizer(article_content[:300], max_length=100, min_length=30, do_sample=False)        
        keywords = [kw[0] for kw in kw_extractor.extract_keywords(article_content[:300])]  # Use only first 300 characters        polarity = TextBlob(summary).sentiment.polarity

        textblob_analysis = TextBlob(summary).sentiment
        polarity = textblob_analysis.polarity

        sentiment = "Positive" if polarity > 0 else "Negative" if polarity < -0.1 else "Neutral"
        sentiment_counts[sentiment] += 1

        data_list.append({
            "Article Number": idx,
            "Title": title,
            "URL": url,
            "Summary": summary,
            "Sentiment": sentiment,
            "Keywords": keywords
        })

    sentiment_report = {
        "Company": company.capitalize(),
        "Articles": data_list,
        "Sentiment Distribution": sentiment_counts,
        "Most Positive Article": max(data_list, key=lambda x: TextBlob(x["Summary"]).sentiment.polarity, default={}),
        "Most Negative Article": min(data_list, key=lambda x: TextBlob(x["Summary"]).sentiment.polarity, default={})
    }

    with open(output_json, "w", encoding="utf-8") as json_file:
        json.dump(sentiment_report, json_file, ensure_ascii=False, indent=4)

    return output_json

# ✅ **Generate Hindi TTS**
def generate_tts(company):
    dir_path = f"data/{company}_articles"
    json_path = f"{dir_path}/{company}_articles_sentiment.json"
    tts_path = f"{dir_path}/{company}_sentiment_hindi.mp3"

    with open(json_path, "r", encoding="utf-8") as f:
        sentiment_dist = json.load(f)["Sentiment Distribution"]

    sentiment_text = f"{company} की खबरें {sentiment_dist} हैं।"    
    tts = gTTS(sentiment_text, lang="hi", slow=False)
    tts.save(tts_path)

    return tts_path