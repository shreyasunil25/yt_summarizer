
from youtube_transcript_api import (
    YouTubeTranscriptApi,
    TranscriptsDisabled,
    NoTranscriptFound
)

def get_transcript_text(video_id):
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return " ".join([t['text'] for t in transcript])

    except (TranscriptsDisabled, NoTranscriptFound):
        return "Error: No transcript available for this video."

    except Exception as e:
        return f"Error: {str(e)}"

def extract_video_id(youtube_url):
    """
    Examples of URLs:
    - https://www.youtube.com/watch?v=KzX82...
    - https://youtu.be/KzX82...
    """
    if "v=" in youtube_url:
        return youtube_url.split("v=")[1].split("&")[0]
    elif "youtu.be" in youtube_url:
        return youtube_url.split("/")[-1]
    else:
        return None
