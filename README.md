📰 News Sentiment Analyzer

This is a News Sentiment Analysis and Text-to-Speech (TTS) App built using Flask, Streamlit,** and Hugging Face Spaces. The application extracts news, analyzes sentiment, and converts text into speech.

🚀 Features

- Fetches latest news from **Google News**
- Performs sentiment analysis using **TextBlob** 
- Converts text to speech using **gTTS**
- Provides a simple UI using **Streamlit** 
- Deployed on **Hugging Face Spaces**

📌 Installation & Setup

**1️. Clone the Repository**

git clone https://github.com/vibhasingh99/news-sentiment-app.git

cd news-sentiment-app

**2️. Create a Virtual Environment**

python -m venv venv

source venv/bin/activate   # Mac/Linux

venv\Scripts\activate     # Windows

**3️. Install Dependencies**

pip install -r requirements.txt

**4️. Run Flask Backend**

python backend.py

Flask will run at: [**http://127.0.0.1:5000/**](http://127.0.0.1:5000/)

**5️. Run Streamlit Frontend**

streamlit run app.py

Streamlit will open in the browser.

📡 API Endpoints

**1️. Check if Backend is Running**

GET /

🔹 **Response:**

{"message": "Flask backend is running!"}

**2️. Perform Sentiment Analysis**

POST /analyze\_sentiment

🔹 **Body (JSON):**

{"text": "This product is amazing!"}

🔹 **Response:**

{"sentiment": "Positive", "text": "This product is amazing!"}

**3️. Convert Text to Speech**

POST /text-to-speech

🔹 **Body (JSON):**

{"text": "Hello, welcome to my app!"}

🔹 **Response:** MP3 file will be generated and sent as a download.

🎤 Deployment on Hugging Face Spaces

1️. Create a Hugging Face Space

` `2️. Upload app.py, backend.py, requirements.txt

` `3️. Restart Space from Settings

` `4️. Test API & Frontend

` `**Live App:** [https://huggingface.co/vibha08]

📌 Next Steps

- ` `Improve sentiment analysis with a more powerful ML model 
- ` `Enhance UI with better design 
- ` `Deploy on cloud platforms like AWS/GCP

🛠 Tech Stack

- **Python**
- **Flask** (Backend API)
- **Streamlit** (Frontend UI)
- **TextBlob** (Sentiment Analysis)
- **gTTS** (Text-to-Speech)
- **BeautifulSoup** (Web Scraping)
- **Hugging Face Spaces** (Deployment)
-----
Developed by **Vibha Singh Chauhan**

🔗 **GitHub:** [https://github.com/vibhasingh99/news-sentiment-app]
🔗 **Hugging Face Space:** [https://huggingface.co/vibha08]

