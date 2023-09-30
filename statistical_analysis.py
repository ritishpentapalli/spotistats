import requests
import pandas as pd
from pprint import pprint

with open("user_access_token.txt") as file:
    user_access_token = file.read()

###### Getting user's top 50 tracks from Spotify API ######
top_songs = []
top_songs_api_call = requests.get(f'https://api.spotify.com/v1/me/top/tracks?limit=50&time_range=medium_term', headers={"Authorization": f"Bearer {user_access_token}"}).json()['items']
for song in top_songs_api_call: top_songs.append([song['id'],song['popularity']]) # Nested list of top 50 songs [<song ID>:str, <popularity>:int] # Potential: Fetch song name as well?

songs_pandas = pd.DataFrame(top_songs, columns=['ID', 'Popularity'])

###### Getting user's top 10 artists from Spotify API ######
top_artists = []
top_artists_api_call = requests.get(f'https://api.spotify.com/v1/me/top/artists?limit=10&time_range=medium_term', headers={"Authorization": f"Bearer {user_access_token}"}).json()['items']
for artist in top_artists_api_call: top_artists.append([artist['name'], artist['id'], artist['popularity'] ]) # Nested list of top 10 artists [<artist name>:str, <artist ID>:str, <popularity>:int]

artists_pandas = pd.DataFrame(top_artists, columns=['Name', 'ID', 'Popularity'])




