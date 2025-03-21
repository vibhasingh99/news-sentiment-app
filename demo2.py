import streamlit as st
import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS
import os
import time
import platform
from deep_translator import GoogleTranslator

def fetch_google_news(microsoft):
    """Fetch 10 news articles from Google News for the given company."""
    
    search_url = f"https://www.google.com/search?q={microsoft}+news&hl=en&tbm=nws"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    response = requests.get(search_url, headers=headers)
    
    if response.status_code != 200:
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = []

    results = soup.find_all('div', class_='SoaBEf', limit=10)
    
    for result in results:
        try:
            title_tag = result.find('div', class_='nDgy9d')
            link_tag = result.find('a', href=True)
            
            if title_tag and link_tag:
                title = title_tag.text.strip()
                raw_link = link_tag['href']

                if raw_link.startswith("/url?q="):
                    link = raw_link.split("&")[0][7:]
                elif raw_link.startswith("http"):
                    link = raw_link
                else:
                    link = "https://www.google.com" + raw_link
                
                articles.append({"title": title, "link": link})
        except AttributeError:
            continue  
    
    return articles

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity > 0:
        return "Positive 😀"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def generate_tts(text, language='hi'):
    if not text.strip():
        return None
    
    translated_text = GoogleTranslator(source='en', target='hi').translate(text)
    tts = gTTS(text=translated_text, lang=language, slow=False)
    audio_file = "news_audio.mp3"
    tts.save(audio_file)
    return audio_file

# 🎨 Streamlit UI
st.set_page_config(page_title="News Sentiment Analyzer", layout="wide")
st.title("📰 News Sentiment Analyzer")

company = st.text_input("🔍 Enter the company name:")

if company:
    if st.button("Analyze News"):
        with st.spinner("Fetching news, please wait..."):
            news = fetch_google_news(company)

        if not news:
            st.error("❌ No news found!")
        else:
            news_text = ""
            for article in news:
                sentiment = analyze_sentiment(article['title'])
                news_text += article['title'] + ". "
                st.subheader(article['title'])
                st.markdown(f"🔗 [Read More]({article['link']})")
                st.write(f"📊 Sentiment: {sentiment}")
                st.divider()
            
            if news_text.strip():
                audio_file = generate_tts(news_text)
                if audio_file:
                    with open(audio_file, "rb") as audio:
                        st.audio(audio, format="audio/mp3")
                        st.download_button("⬇️ Download Audio", audio, file_name="news_audio.mp3", mime="audio/mp3")
