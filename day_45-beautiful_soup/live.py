#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_webpage = response.text

yc_soup = BeautifulSoup(yc_webpage, "html.parser")

articles = yc_soup.select(".titleline a")

article_texts = []
article_links = []
for article_tag in articles:
    article_texts.append(article_tag.getText())
    article_links.append(article_tag.get("href"))
article_upvote = [int(score.getText().split()[0]) for score in yc_soup.find_all("span", class_="score")]

top_vote = article_upvote.index(max(article_upvote))

print(article_texts[top_vote])
print(article_links[top_vote])
print(article_upvote[top_vote])
