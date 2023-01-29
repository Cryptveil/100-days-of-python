from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
news = soup.find(class_="titleline")
print(news.find(name="a").getText())
print(news.find(name="a").get("href"))
score = soup.find(class_="score")
print(score.getText())
