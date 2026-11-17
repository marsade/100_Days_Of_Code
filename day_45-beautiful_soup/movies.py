#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in movies]
movie_titles.reverse()
print(movie_titles)

with open("movies.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(movie_titles))