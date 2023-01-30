import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = os.environ["SPOTIPY_CLIENT_ID"]
CLIENT_SECRET = os.environ["SPOTIPY_CLIENT_SECRET"]
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"

date = input("Which year do you want to travel to? "
             "Type the date in the format 'YYYY-MM-DD': ")

BILBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(BILBOARD_URL)
soup = BeautifulSoup(response.text, "html.parser")
song_names = soup.find_all(name="h3",
                           id="title-of-a-story",
                           class_="lrv-u-font-size-16")

song_list = [song.getText().strip("\n\t") for song in song_names]

oauth_object = spotipy.SpotifyOAuth(client_id=CLIENT_ID,
                                    client_secret=CLIENT_SECRET,
                                    redirect_uri=REDIRECT_URI,
                                    scope=SCOPE,
                                    cache_path="token.txt")
sp = spotipy.Spotify(auth_manager=oauth_object)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
