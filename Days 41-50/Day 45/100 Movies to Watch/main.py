import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/"
"https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movie_list = []
for entry in movies:
    movie_text = entry.getText()
    movie_list.append(movie_text)

result = "\n".join(movie_list[::-1])

with open("movies.txt", "w") as file:
    for line in result:
        file.write(line)
