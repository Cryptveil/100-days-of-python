from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

news = soup.find_all(class_="titleline")
for heading in news:
    print(heading.find(name="a").get("href"))
    print(heading.find(name="a").getText())

scores = soup.find_all(class_="score")
for score in scores:
    print(score.getText().split(" ")[0])
