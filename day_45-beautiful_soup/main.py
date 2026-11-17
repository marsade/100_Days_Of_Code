#!/usr/bin/env python3
from bs4 import BeautifulSoup

with open("website.html") as f:
    contents = f.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.prettify())
# print(soup.title)
# all_anchor_tags = soup.find_all(name="a")

# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

heading = soup.find(name="h1", id="name")
# print(heading.get("id"))

section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())

name = soup.select_one("#name").getText()
headings = soup.select(".heading")

print(name, headings)