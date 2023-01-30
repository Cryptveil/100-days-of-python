import requests
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? "
             "Type the date in the format 'YYYY-MM-DD': ")

BILBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(BILBOARD_URL)
soup = BeautifulSoup(response.text, "html.parser")
song_names = soup.find_all(name="h3",
                           id="title-of-a-story",
                           class_="lrv-u-font-size-16")

song_list = [song.getText().strip("\n\t") for song in song_names]

