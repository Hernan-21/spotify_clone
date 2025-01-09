import spotipy # type: ignore
from spotipy.oauth2 import SpotifyOAuth # type: ignore
import os
from dotenv import load_dotenv # type: ignore

load_dotenv()

def get_spotify_client():
    auth_manager = SpotifyOAuth(
        client_id=os.getenv('SPOTIFY_CLIENT_ID'),
        client_secret=os.getenv('SPOTIFY_CLIENT_SECRET'),
        redirect_uri=os.getenv('SPOTIFY_REDIRECT_URI'),
        scope=' '.join([
            'user-library-read',
            'playlist-modify-public',
            'user-read-playback-state',
            'user-top-read',
            'user-read-currently-playing',
            'user-read-recently-played',
            'playlist-read-private',
            'user-follow-read'
        ]),
        open_browser=True,
        cache_path='.spotify_cache'
    )
    
    return spotipy.Spotify(auth_manager=auth_manager) 