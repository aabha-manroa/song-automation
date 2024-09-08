import yt_dlp

def download_songs(singer, number_of_songs):
    search_query = f"{singer} songs"
    
    # yt-dlp options
    ydl_opts = {
        'format': 'bestaudio/best',  # Get the best available audio format
        'outtmpl': 'songdwl/%(title)s.%(ext)s',  # Save in songdwl folder
        'noplaylist': True,  # No playlists
        'extractaudio': True,  # Only extract audio
        'audioformat': 'mp3'  # Save as mp3 (if available)
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.extract_info(f"ytsearch{number_of_songs}:{search_query}", download=True)

singer = "BTS"
number_of_songs = 5

download_songs(singer, number_of_songs)
