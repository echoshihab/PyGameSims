import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup


user_input_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

#get top 100 songs from the date
billboard_response = requests.get(f"https://www.billboard.com/charts/hot-100/{user_input_year}")
soup = BeautifulSoup(billboard_response.text, 'lxml')

li_items = soup.select(".chart-list__element")

names =[]
artists = []
spotify_song_uris = []

for li in li_items:
    names.append(li.select_one('.chart-element__information__song').getText())
    artists.append(li.select_one('.chart-element__information__artist').getText())

#access spotify with playlist modification permissions
spotify_client_id = os.environ.get('spotify_id')
spotify_client_secret = os.environ.get('spotify_secret')
spotify_redirect_uri = 'http://example.com'
scope = "playlist-modify-private"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=spotify_redirect_uri,
                                               scope=scope))

current_user = sp.current_user()

playlist_response = sp.user_playlist_create(user=current_user['id'], name=f"Billboard Top 100 {user_input_year}", public=False)


for index in range(len(artists)):
    search_result =sp.search(f"track:{names[index]} artist:{artists[index]}", limit=1, type="track")
    try:
        spotify_song_uris.append(search_result['tracks']['items'][0]['uri'])
    except:
        print(f"Unable to find and add {names[index]} by {artists[index]} to playlist, skipping this song")

sp.playlist_add_items(playlist_id=playlist_response['id'], items=spotify_song_uris)


