import requests
import pandas as pd

with open("user_access_token.txt") as file: user_access_token = file.read()

###########################################################
###### Getting user's top 50 tracks from Spotify API ######
###########################################################

top_songs = []
top_songs_api_call = requests.get(f'https://api.spotify.com/v1/me/top/tracks?limit=50&time_range=medium_term', headers={"Authorization": f"Bearer {user_access_token}"}).json()['items']

for song in top_songs_api_call:
    top_songs.append([ # Nested list of top 50 songs [<song name>:str, <song ID>:str, <popularity>:int]
          song['name'],
          song['id'],
          song['popularity']
          ]) 

for song in top_songs:
        song_data = requests.get(f'https://api.spotify.com/v1/audio-features/{song[1]}',
                                 headers={"Authorization": f"Bearer {user_access_token}"}).json()
        song += [ # Adding song features
                 song_data['acousticness'],
                 song_data['danceability'],
                 song_data['duration_ms'],
                 song_data['energy'],
                 song_data['instrumentalness'],
                 song_data['liveness'],
                 song_data['loudness'],
                 song_data['speechiness'],
                 song_data['tempo'],
                 song_data['valence']
                ]

songs_pandas = pd.DataFrame(top_songs, columns=['Name',
                                                'ID',
                                                'Popularity',
                                                'Acousticness',
                                                'Danceability',
                                                'Duration(in ms)',
                                                'Energy',
                                                'Instrumentalness',
                                                'Liveliness',
                                                'Loudness',
                                                'Speechiness',
                                                'Tempo',
                                                'Valence'
                                                ])

############################################################
###### Getting user's top 10 artists from Spotify API ######
############################################################

top_artists = []
top_artists_api_call = requests.get(f'https://api.spotify.com/v1/me/top/artists?limit=10&time_range=medium_term',
                                    headers={"Authorization": f"Bearer {user_access_token}"}).json()['items']

for artist in top_artists_api_call: top_artists.append([
     artist['name'], # Nested list of top 10 artists [<artist name>:str, <artist ID>:str, <popularity>:int]
     artist['id'],
     artist['popularity']
     ])

artists_pandas = pd.DataFrame(top_artists, columns=['Name',
                                                    'ID',
                                                    'Popularity'
                                                    ])

print(songs_pandas)
print(artists_pandas)



# Summarizing user's music data