import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi
from utils import extract_video_id, get_transcript_text

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel('gemini-1.5-flash-lite')

st.set_page_config(page_title="Youtube Summarizer", page_icon="▶️")
st.title("▶️ YouTube Summarizer & Chat")
youtube_link = st.text_input("Paste YouTube Video Link:")
if youtube_link:
    video_id = extract_video_id(youtube_link)

    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", width="stretch")

        if st.button("Analyze Video"):
            with st.spinner("Downloading Transcript..."):
                transcript_text = get_transcript_text(video_id)

            if "Error:" in transcript_text:
                st.error(transcript_text)
            else:
                st.session_state['transcript'] = transcript_text

                with st.spinner("Generating Summary..."):
                    prompt = f"""
                    You are a YouTube video summarizer.
                    Summarize the video in clear bullet points within 250 words.

                    TRANSCRIPT:
                    {transcript_text}
                    """
                    response = model.generate_content(prompt)
                    st.session_state['summary'] = response.text

# --- Display Results ---
if 'summary' in st.session_state:
    st.markdown("### 📝 Video Summary")
    st.write(st.session_state['summary'])
    
    st.markdown("---")
    st.markdown("### 💬 Ask questions about the video")
    
    user_question = st.text_input("Ask something specific (e.g., 'What did he say about pricing?')")
    
    if user_question:
        if 'transcript' in st.session_state:
            with st.spinner("Thinking..."):
                # RAG Logic: Pass the transcript + Question
                q_prompt = f"""
                Answer the question based ONLY on the video transcript provided below.
                
                TRANSCRIPT:
                {st.session_state['transcript']}
                
                QUESTION:
                {user_question}
                """
                answer = model.generate_content(q_prompt)
                st.write(answer.text)