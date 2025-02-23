import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import pprint as pp

load_dotenv('.env')
SPOTIPY_CLIENT_ID=os.getenv('SPOTIPY_CLIENT_ID')
SPOTIPY_CLIENT_SECRET=os.getenv('SPOTIPY_CLIENT_SECRET')
SPOTIPY_REDIRECT_URI=os.getenv('SPOTIPY_REDIRECT_URI')

scope = "user-library-read, user-read-playback-state"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=SPOTIPY_CLIENT_ID, client_secret=SPOTIPY_CLIENT_SECRET,
    redirect_uri=SPOTIPY_REDIRECT_URI, scope=scope))

playing = sp.current_playback()
song = playing['item']['name']
artist = playing['item']['album']['artists'][0]['name']

print(f'Now PLaying: {artist} - {song}')