import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
from utils import limpar_terminal

scopes = ["https://www.googleapis.com/auth/youtube.readonly"]


def main():
    limpar_terminal()
    playlist_link = input("De qual playlist deseja obter informações?\n~> ").strip()
    playlist_id = playlist_link.split("list=")[-1]
    
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "secrets.json"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
    credentials = flow.run_local_server()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)
    
    video_ids = []
    videos_info = {}
    next_page_token = None
    
    while True:
        request = youtube.playlistItems().list(
            part = "contentDetails",
            maxResults = 50,
            playlistId = playlist_id,
            pageToken=next_page_token
        )
        response = request.execute()
        video_ids.extend([video["contentDetails"]["videoId"] for video in response.get("items", [])])
        
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    for i in range(0, len(video_ids), 50):
        batch_ids = video_ids[i:i + 50]
        
        request = youtube.videos().list(
            part = "snippet, statistics",
            id = ",".join(batch_ids)
        )
        response = request.execute()
        
        for video in response.get("items", []):
            title = video["snippet"]["title"]
            views = video["statistics"]["viewCount"]
            videos_info[title] = views
    
    limpar_terminal()
    print("========================= Relatório Completo da Playlist =========================")
    for position, (title, views) in enumerate(videos_info.items(), start = 1):
        print(f"{position} - {title}: {views} visualizações.")


if __name__ == "__main__":
    main()
