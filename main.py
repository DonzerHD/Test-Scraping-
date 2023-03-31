import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.imdb.com/chart/top/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(url, headers=headers)

def get_movie_details(movie_url):
    response = requests.get(movie_url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        genre_section = soup.find('li', {'data-testid': 'storyline-genres', 'role': 'presentation'})
        # OU
        # genre_section = soup.find_all('li', {'data-testid': 'storyline-genres'})[0]

        genre_link = genre_section.find('a', class_='ipc-metadata-list-item__list-content-item--link')
        genre = genre_link.text
        print(genre)

        
    else:
        print("Erreur lors de la récupération de la page")
        return []

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    movie_data = []
    titles = soup.find_all('td', {'class': 'titleColumn'})
    ratings = soup.find_all('td', {'class': 'ratingColumn imdbRating'})

    for i in range(2):
        title = titles[i].find('a').text
        year = titles[i].find('span', {'class': 'secondaryInfo'}).text
        year = year.replace('(', '').replace(')', '').strip()
        rating = ratings[i].find('strong').text
        link = titles[i].find('a')['href']
        link = 'https://www.imdb.com' + link

        # Récupérer les genres et les acteurs
        genres = get_movie_details(link)

        movie_data.append((title, year, rating , genres ,  link))

    # Écrire les données dans un fichier CSV
    with open('movies.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['Title', 'Year', 'Rating' , 'Genres', 'Link'])

        for movie in movie_data:
            csv_writer.writerow(movie)

else:
    print("Erreur lors de la récupération de la page")