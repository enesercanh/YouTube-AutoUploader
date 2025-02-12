# upload.py - YouTube Video Auto Uploader

import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Authenticate with YouTube API
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CLIENT_SECRETS_FILE = "client_secret.json"

def authenticate():
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRETS_FILE, SCOPES
    )
    credentials = flow.run_local_server(port=0)
    return googleapiclient.discovery.build("youtube", "v3", credentials=credentials)

def upload_video(youtube, file_path, title, description, tags, category_id="22", privacy_status="public"):
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": tags,
                "categoryId": category_id
            },
            "status": {
                "privacyStatus": privacy_status
            }
        },
        media_body=googleapiclient.http.MediaFileUpload(file_path, chunksize=-1, resumable=True)
    )
    response = request.execute()
    print(f"✅ Uploaded: {title} (Video ID: {response['id']})")

if __name__ == "__main__":
    youtube = authenticate()
    for video_file in os.listdir("output_videos"):
        if video_file.endswith(".mp4"):
            upload_video(youtube, f"output_videos/{video_file}", title=video_file, description="Uploaded via API", tags=["Automation", "YouTube"])
