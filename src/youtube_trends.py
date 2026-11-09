from googleapiclient.discovery import build

API_KEY = "YOUR_API_KEY"

youtube = build(
    "youtube",
    "v3",
    developerKey=API_KEY
)

print("Connected to YouTube API")
