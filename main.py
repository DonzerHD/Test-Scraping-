import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/top/"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    movie_data = []
    titles = soup.find_all('td', {'class': 'titleColumn'})
    ratings = soup.find_all('td', {'class': 'ratingColumn imdbRating'})

    for i in range(len(titles)):
        title = titles[i].find('a').text
        year = titles[i].find('span', {'class': 'secondaryInfo'}).text
        rating = ratings[i].find('strong').text

        movie_data.append((title, year, rating))

    with open('movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Title', 'Year', 'Rating'])

        for movie in movie_data:
            csv_writer.writerow(movie)

else:
    print("Erreur lors de la récupération de la page")