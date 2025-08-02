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
    
    request = youtube.playlistItems().list(
        part = "contentDetails",
        maxResults = 50,
        playlistId = playlist_id
    )
    response = request.execute()
    
    videos = response.get("items", [])
    videos_id = [video["contentDetails"]["videoId"] for video in videos]
    
    request = youtube.videos().list(
        part = "snippet, statistics",
        id = ",".join(videos_id)
    )
    response = request.execute()

    videos = response["items"]
    videos_info = {video["snippet"]["title"]: video["statistics"]["viewCount"] for video in videos}
    
    limpar_terminal()
    print("========================= Relatório Completo da Playlist =========================")
    for position, (title, views) in enumerate(videos_info.items(), start = 1):
        print(f"{position} - {title}: {views} visualizações.")


if __name__ == "__main__":
    main()
