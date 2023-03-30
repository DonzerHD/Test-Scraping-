import requests
from bs4 import BeautifulSoup

base_url = 'http://quotes.toscrape.com'
url = base_url

while url:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extraire les auteurs des citations
        auteurs = soup.find_all('small', {'class': 'author'})

        # Afficher les auteurs mais sans doublons mais vérifier si l'auteur est déjà dans la liste
        for auteur in auteurs:
            if auteur not in auteurs:
                auteurs.append(auteur)
        print(auteur.text)

        # Trouver le lien vers la page suivante
        next_page = soup.find('li', {'class': 'next'})

        if next_page:
            # Récupérer l'URL de la page suivante et mettre à jour l'URL pour le prochain tour de boucle
            url = base_url + next_page.find('a')['href']
        else:
            # S'il n'y a pas de page suivante, mettre fin à la boucle
            url = None

    else:
        print("Erreur lors de la récupération de la page")
        url = None