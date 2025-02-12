# YouTube-AutoUploader

This repository automates video uploads to YouTube using the YouTube Data API v3 and Python.

## 📌 Prerequisites

1. **Google API Key & OAuth Credentials:**
   - Go to [Google Cloud Console](https://console.cloud.google.com/)
   - Create a new project
   - Enable **YouTube Data API v3**
   - Generate OAuth 2.0 Client ID (Download `client_secret.json`)

2. **Install Dependencies:**
   ```sh
   pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

## 🚀 Usage

1. Place `client_secret.json` in the root folder.
2. Move all `.mp4` videos to the `output_videos` folder.
3. Run the script:
   ```sh
   python upload.py
   ```
4. Authenticate via browser when prompted.
5. The script will automatically upload all videos from `output_videos`.

## 📂 Repository Structure
```
📂 YouTube-AutoUploader
 ├── 📂 output_videos   # Folder for videos to be uploaded
 ├── 📜 upload.py       # Python script for uploading videos
 ├── 📜 client_secret.json  # (DO NOT COMMIT - Add to .gitignore)
 ├── 📜 README.md       # Step-by-step guide
 ├── 📜 .gitignore      # Prevents pushing secrets
```

## 🛑 Important
- **Do NOT share `client_secret.json`** (Add it to `.gitignore`).
- Google has upload quotas per day; check [YouTube API Quotas](https://developers.google.com/youtube/registering_an_application).
- Modify `upload.py` to customize video title, description, and privacy settings.

## 🔗 References
- [YouTube Data API Docs](https://developers.google.com/youtube/v3/)
- [OAuth 2.0 Guide](https://developers.google.com/identity/protocols/oauth2)

🚀 Happy Automating!
