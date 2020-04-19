import requests
from requests import get
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

headers = {"Accept-Language":"en-US, en;q=0.5"}

url = "https://www.imdb.com/search/title/?groups=top_1000&ref_=adv_prv"	# url is the variable we create and assign the URL to
results = requests.get(url, headers = headers)			#results is the variable we create to store our request.get action
results = requests.get(url)

soup = BeautifulSoup(results.text, "html.parser")
#print(soup.prettify())

# lists where we need to store our data

titles = []
years = []
time = []
imdb_ratings = []
metascores = []
votes = []
us_gross = []

movie_div = soup.find_all('div', class_ = 'lister-item mode-advanced')

for container in movie_div:
	name = container.h3.a.text
	titles.append(name)
	year = container.h3.find('span', class_ = 'lister-item-year').text
	years.append(year)
	runtime = container.find('span', class_ = 'runtime').text if container.p.find('span', class_ = 'runtime') else '-'
	time.append(runtime)
	ratings = container.strong.text
	imdb_ratings.append(ratings)
	m_score = container.find('span',class_='metascore').text if container.find('span',class_='metascore') else '-'
	metascores.append(m_score)
	vote_gross = container.find_all('span',attrs = {'name':'nv'})
	vote = vote_gross[0].text
	votes.append(vote)
	gross = vote_gross[1].text if len(vote_gross) > 1 else '-'
	us_gross.append(gross)

movies = pd.DataFrame({
	'movie':titles,
	'year':years,
	'timemin':time,
	'imdb':imdb_ratings,
	'metascore':metascores,
	'votes':votes,
	'us_gross_million':us_gross
	})

# print(movies.dtypes)
# print(movies)

movies['year'] = movies['year'].str.extract('(\d+)').astype(int)
movies['timemin'] = movies['timemin'].str.extract('(\d+)').astype(int)
movies['imdb'] = movies['imdb'].str.extract('(\d+)').astype(float)
movies['metascore'] = pd.to_numeric(movies['metascore'], errors = 'coerce')
movies['votes'] = movies['votes'].str.replace(',','').astype(int)
movies['us_gross_million'] = movies['us_gross_million'].map(lambda x:x.lstrip('$').rstrip('M'))
movies['us_gross_million'] = pd.to_numeric(movies['us_gross_million'], errors = 'coerce')


print(movies.dtypes)
print(movies)
#print(movies['timemin'])
movies.to_csv("movies.csv")
# print(titles)
# print(years)
# print(time)
# print(imdb_ratings)
# print(metascores)
# print(votes)
# print(us_gross)
#print(movie_div)

#print(results)