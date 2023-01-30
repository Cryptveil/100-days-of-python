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
    upvotes = int(score.getText().split(" ")[0])
    article_upvotes.append(upvotes)

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
print(article_links[largest_index])
print(f"Likes: {largest_number}")

# print(article_texts)
# print(article_links)
# print(article_upvotes)
