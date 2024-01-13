from dotenv import load_dotenv
load_dotenv()
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

delim = 0 
results = sp.current_user_saved_tracks(50, delim)
while results['items']:
    for idx, item in enumerate(results['items'], delim):
        track = item['track']
        print(idx, track['artists'][0]['name'], " – ", track['name'])
    delim += 50
    results = sp.current_user_saved_tracks(50, delim)
