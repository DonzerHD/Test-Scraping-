# IMDb Advanced Web Scraping Project

The goal of this project is to create a database of movies and actors using web scraping. Follow these steps to create the project:

## 1. Scrape IMDb Top 250 Movies

Create a scraping program to extract the following information for each movie in the IMDb Top 250:

- Title
- Year
- Rating
- Link to the movie page
- Genre(s)
- Runtime
- Director
- List of main actors (e.g., top 5 actors)

## 2. Scrape Individual Movie Pages

Modify the program to access each movie's page (using the previously extracted link) and retrieve the following additional information:

- Plot summary
- Box office (if available)
- Budget (if available)
- Original language(s)
- Country of origin

## 3. Store Data in a Database

Store all collected information in a database. You can use SQLite to create a local database. Create two tables in the database:

- `movies` table: to store information about movies
- `actors` table: to store information about actors

## 4. Interact with the Database

Create a Python program to interact with the database and perform operations such as:

- Search movies by title, year, director, or genre
- Search actors by name
- Display movies featuring a specific actor
- Display statistics about movies, e.g., number of movies per genre or rating distribution

## 5. (Optional) Create a User Interface

Create a user interface for your project, such as a web application or an interactive dashboard, to facilitate data access and visualization of results.

**Note**: Don't forget to handle exceptions and errors during scraping and use pauses and delays to avoid overloading the IMDb website with requests. Good luck with this advanced project!