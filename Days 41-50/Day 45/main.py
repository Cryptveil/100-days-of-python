from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")

article_texts = []
article_links = []
article_upvotes = []

news = soup.find_all(class_="titleline")
for heading in news:
    link = heading.find(name="a").get("href")
    article_links.append(link)
    text = heading.find(name="a").getText()
    article_texts.append(text)

scores = soup.find_all(class_="score")
for score in scores:
    upvotes = score.getText().split(" ")[0]
    article_upvotes.append(upvotes)

print(article_texts)
print(article_links)
print(article_upvotes)
