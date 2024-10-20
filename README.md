
# ChooseUrMovie - Movie Recommendation System

## Overview
ChooseUrMovie is a movie recommendation system that suggests films based on a user's favorite movie. By analyzing a dataset of films, the system computes similarities between movies using text features such as genres, keywords, actors, directors, and taglines.

This system uses the `TfidfVectorizer` from `SkLearn` to convert movie descriptions into numerical vectors and calculates the similarity between movies using **cosine similarity**. In addition, the system handles possible user input errors using `difflib` to suggest correct movie titles in case of spelling mistakes.

## Features
- Recommend movies similar to a user's favorite movie.
- Automatically corrects for potential spelling errors in movie titles.
- Display detailed information about recommended films.
- Allow users to request additional recommendations.
- Customizable to any dataset with film-related information.

## Dataset
The dataset should be in CSV format with at least the following columns:
- `title` : The title of the movie.
- `genres` : Genres the movie belongs to (e.g., Action, Drama).
- `keywords` : Keywords that describe the movie.
- `tagline` : The tagline of the movie.
- `cast` : Main actors in the movie.
- `director` : The director of the movie.

In this project, the dataset used is `movies.csv`, which contains these relevant features. You can replace it with another dataset as long as the required columns are present.

## Requirements
- Python 3.x
- Pandas
- Scikit-learn
- Difflib (standard library)

To install the necessary dependencies, run:

```
pip install pandas scikit-learn
```

## How to Use
1. Place your dataset (`movies.csv`) in the same directory as the Python script.
2. Run the Python script (`choose_ur_movie.py`).
3. When prompted, enter the name of your favorite movie.
4. The system will provide recommendations of similar films. If there are errors in the movie title, the system will suggest the closest matches.
5. You can view more details on each recommended film and request additional movie recommendations.

## Code Structure
- **`movies.csv`**: The dataset containing movie information.
- **`choose_ur_movie.py`**: The main Python script for running the recommendation system.
- **`README.md`**: This file explaining the project and how to use it.

## Example
```
Entrez le nom de votre film préféré : Avatar
Film sélectionné : Avatar

Les 10 films les plus similaires à votre film préféré sont :

1. Pirates of the Caribbean: At World's End (Score de similarité : 0.75)
2. Spectre (Score de similarité : 0.70)
...
```

## Customization
You can modify the script to fit your specific needs:
- Add additional columns to the `combined_features` to include more text information (like the movie's plot or reviews).
- Change the number of recommendations returned by modifying the relevant parts of the script.

## License
This project is open-source and available under the MIT License.
