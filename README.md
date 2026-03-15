# YouTube Video Summarizer 🎥

Paste any YouTube URL to get an AI-generated summary and ask questions about the video content — powered by Google Gemini.

## Features
- Extracts transcript automatically from any YouTube video
- Generates a concise bullet-point summary (under 250 words)
- Q&A mode: ask specific questions about the video content
- Built with Streamlit for a clean, interactive UI

## Tech Stack
- Python
- Streamlit
- Google Gemini API (gemini-1.5-flash)
- YouTube Transcript API

## Setup

1. Clone the repo
   git clone https://github.com/shreyasunil25/yt_summarizer.git
   cd yt_summarizer

2. Install dependencies
   pip install -r requirements.txt

3. Add your API key — create a .env file:
   GOOGLE_API_KEY=your_key_here

4. Run the app
   streamlit run app.py

## How It Works
The app fetches the video transcript using YouTubeTranscriptAPI, passes it to Gemini with a summarization prompt, and displays structured bullet points. The Q&A feature sends the full transcript + user question to Gemini and returns a grounded answer based only on the video content.
