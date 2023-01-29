from bs4 import BeautifulSoup

with open("website.html") as website:
    data = website.read()

soup = BeautifulSoup(data, "html.parser")

print(soup.title)
