import requests
import os
import sys
import csv
import spotipy
import timeit

from spotipy.oauth2 import SpotifyClientCredentials

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=os.environ.get('SPOTIPY_CLIENT_ID'),
                                                           client_secret=os.environ.get('SPOTIPY_CLIENT_SECRET')))

# timeit library to measure the time needed to run this code

start = timeit.default_timer()

# create empty lists where the results are going to be stored
artist_name = []
track_name = []
popularity = []
track_id = []

for i in range(0,10000,50):
    track_results = sp.search(q='year:2020', type='track', limit=50,offset=i)
#     for i, t in enumerate(track_results['tracks']['items']):
#         artist_name.append(t['artists'][0]['name'])
#         track_name.append(t['name'])
#         track_id.append(t['id'])
#         popularity.append(t['popularity'])
      

stop = timeit.default_timer()
print ('Time to run this code (in seconds):', stop - start)