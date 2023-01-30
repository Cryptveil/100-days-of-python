from requests_html import HTMLSession
from bs4 import BeautifulSoup

date = input("Which year do you want to travel to? "
             "Type the date in the format 'YYYY-MM-DD': ")

BILBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}"


def get_web_page():
    session = HTMLSession()
    response = session.get(BILBOARD_URL)
    response.html.render()
    with open("100_songs.html", mode="w", encoding="utf-8") as file:
        file.write(response.html)


def read_web_file():
    try:
        open("100_songs.html")
    except FileNotFoundError:
        get_web_page()
    finally:
        with open("100_songs.html", mode="r", encoding="utf-8") as file:
            data = file.read()
            return BeautifulSoup(data, "html.parser")


soup = read_web_file()
song_names = soup.find_all(name="h3", id="title-of-a-story")

song_list = [song.getText() for song in song_names]
