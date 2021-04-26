import requests
import os
import sys
import csv
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
                                                           client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET')))

results = sp.search(q='weezer', limit=20)

for idx, track in enumerate(results['tracks']['items']):
    print(idx, track['name'])