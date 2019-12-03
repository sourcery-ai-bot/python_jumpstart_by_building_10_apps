import requests 
import collections

MovieResult = collections.namedtuple(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")

search = input('What movie do you want to search for? ')
url = f'http://movie_service.talkpython.fm/api/search/{search}'

resp = requests.get(url)
resp.raise_for_status()
# print(resp.status_code)
# print(resp.text)

movie_data = resp.json()
movies_list = movie_data.get('hits')
# print(type(movies), movies)

# movies = []

# for md in movies_list:
#     # m = MovieResult(
#     #         imdb_code=md.get('imdb_code'),
#     #         title=md.get('title'),
#     #         duration=md.get('duration'),
#     #         director=md.get('director'),
#     #         year=md.get('year', 0),
#     #         rating=md.get('rating', 0),
#     #         imdb_score=md.get('imdb_score', 0.0),
#     #         keywords=md.get('keywords'),
#     #         genres=md.get('genres'))

#     m = MovieResult(**md)

#     movies.append(m)


movies = [
    MovieResult(**md)
    for md in movies_list
]
print(f'Found {len(movies)} movies for search [{search}].')

for m in movies:
    print(f'{m.year}, {m.title}')