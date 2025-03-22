from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from gtts import gTTS
import os
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  # CORS enable करो

@app.route('/')
def home():
    return jsonify({"message": "Flask backend is running!"})

@app.route('/analyze_sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Please provide text for sentiment analysis!"}), 400
    
    text = data["text"]
    analysis = TextBlob(text)
    sentiment = "Positive" if analysis.sentiment.polarity > 0 else "Negative" if analysis.sentiment.polarity < 0 else "Neutral"
    
    return jsonify({"text": text, "sentiment": sentiment})

@app.route('/text_to_speech', methods=['POST'])
def text_to_speech():
    data = request.get_json()
    if not data or "text" not in data:
        return jsonify({"error": "Please provide text for conversion!"}), 400

    text = data["text"]
    tts = gTTS(text)
    filename = "output.mp3"
    tts.save(filename)

    return send_file(filename, as_attachment=True)

if __name__ == '__main__':
    print("\n Flask server is starting...")
    with app.app_context():
        print("\n Registered Routes:")
        for rule in app.url_map.iter_rules():
            print(f" {rule.endpoint} - {rule.methods} - {rule.rule}")
    app.run(host="0.0.0.0", port=5000, debug=True)
