import re
import pandas as pd
from googleapiclient.discovery import build

def extract_video_id(url):
    pattern = r'(?:v=|\/)([0-9A-Za-z_-]{11})'
    match = re.search(pattern, url)
    return match.group(1) if match else None

API_KEY = "Your API Key"
VIDEO_URL = "Youtube Video Url"

video_id = extract_video_id(VIDEO_URL)
youtube = build('youtube', 'v3', developerKey=API_KEY)

comments = []
next_page_token = None

while True:
    response = youtube.commentThreads().list(
        part='snippet',
        videoId=video_id,
        maxResults=100,
        pageToken=next_page_token,
        textFormat='plainText'
    ).execute()

    for item in response['items']:
        comment = item['snippet']['topLevelComment']['snippet']
        comments.append({
            'author': comment['authorDisplayName'],
            'text': comment['textDisplay'],
            'likes': comment['likeCount'],
            'published_at': comment['publishedAt'],
        })

    next_page_token = response.get('nextPageToken')
    if not next_page_token:
        break

df = pd.DataFrame(comments)
df.to_csv(f"{video_id}_comments.csv", index=False)
print(f"✅ Collected {len(comments)} comments saved to comments.csv")
