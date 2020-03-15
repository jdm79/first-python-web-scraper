import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd 
import numpy as np 

headers = {"Accept-langauge": "en-US, en;q=0.5"}

url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"
results = requests.get(url, headers=headers)

soup = BeautifulSoup(results.text, "html.parser")

# print(soup.prettify())

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_='lister-item mode-advanced')

for container in movie_div:
  name = container.h3.a.text
  titles.append(name)

for title in titles:
  print title




