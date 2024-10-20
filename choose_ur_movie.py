import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import difflib

# Chargement des données depuis le fichier CSV
movies_data = pd.read_csv('movies.csv')

# Sélection des colonnes pertinentes pour le système de recommandation
movies_data = movies_data[['title', 'genres', 'keywords', 'tagline', 'cast', 'director']]

# Remplacer les valeurs manquantes (NaN) par des chaînes vides
movies_data = movies_data.fillna('')

# Combiner les colonnes sélectionnées pour chaque film en une seule chaîne de texte
movies_data['combined_features'] = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

# Initialisation de l'objet TfidfVectorizer pour transformer les descriptions textuelles en vecteurs
vectorizer = TfidfVectorizer()

# Transformation des textes en vecteurs TF-IDF
feature_vectors = vectorizer.fit_transform(movies_data['combined_features'])

# Calcul des similarités cosinus entre tous les films
similarity = cosine_similarity(feature_vectors)

# Demander à l'utilisateur son film préféré
film_prefere = input("Entrez le nom de votre film préféré : ")

# Utilisation de Difflib pour corriger les fautes d'orthographe ou les erreurs dans le titre
liste_des_films = movies_data['title'].tolist()
film_choisi = difflib.get_close_matches(film_prefere, liste_des_films, n=1)

# Si un film similaire est trouvé, récupérer l'index de ce film
if film_choisi:
    index_film = movies_data[movies_data['title'] == film_choisi[0]].index[0]
    print(f"Film sélectionné : {film_choisi[0]}")
else:
    print("Aucun film trouvé.")
    exit()

# Récupérer les scores de similarité pour ce film
scores_similarites = list(enumerate(similarity[index_film]))

# Trier les films selon les scores de similarité
films_similaires = sorted(scores_similarites, key=lambda x: x[1], reverse=True)

# Afficher les 10 films les plus similaires
print("\nLes 10 films les plus similaires à votre film préféré sont :\n")
top_10 = []
for i, film in enumerate(films_similaires[1:11]):
    index_film_similaire = film[0]
    titre_film = movies_data['title'].iloc[index_film_similaire]
    score_similarite = film[1]
    top_10.append((titre_film, score_similarite))
    print(f"{i+1}. {titre_film} (Score de similarité : {score_similarite:.2f})")

# Option pour afficher plus de détails sur les films recommandés
afficher_details = input("\nVoulez-vous voir plus de détails sur ces films ? (oui/non) : ").lower()

if afficher_details == 'oui':
    for i, film in enumerate(top_10):
        index_film_similaire = movies_data[movies_data['title'] == film[0]].index[0]
        print(f"\n--- Détails du film {i+1} ---")
        print(f"Titre : {movies_data['title'].iloc[index_film_similaire]}")
        print(f"Genre : {movies_data['genres'].iloc[index_film_similaire]}")
        print(f"Acteurs : {movies_data['cast'].iloc[index_film_similaire]}")
        print(f"Réalisateur : {movies_data['director'].iloc[index_film_similaire]}")
        print(f"Slogan : {movies_data['tagline'].iloc[index_film_similaire]}")
        print(f"Mots-clés : {movies_data['keywords'].iloc[index_film_similaire]}")
        print("\n--------------------------")

# Ajouter une option pour recommander plus de films
recommander_plus = input("\nVoulez-vous d'autres recommandations ? (oui/non) : ").lower()

if recommander_plus == 'oui':
    n_recommendations = int(input("Combien de recommandations souhaitez-vous ? : "))
    print(f"\nVoici {n_recommendations} films supplémentaires que vous pourriez aimer :\n")
    for i, film in enumerate(films_similaires[11:11+n_recommendations]):
        index_film_similaire = film[0]
        titre_film = movies_data['title'].iloc[index_film_similaire]
        score_similarite = film[1]
        print(f"{i+1}. {titre_film} (Score de similarité : {score_similarite:.2f})")

# Gérer les cas où aucun film proche n'est trouvé
if not film_choisi:
    print("Nous n'avons pas pu trouver de correspondance proche pour le film que vous avez saisi.")
    suggestions = difflib.get_close_matches(film_prefere, liste_des_films, n=5)
    if suggestions:
        print("Voici des suggestions basées sur ce que vous avez entré :")
        for i, suggestion in enumerate(suggestions):
            print(f"{i+1}. {suggestion}")
    else:
        print("Aucune correspondance trouvée. Veuillez vérifier l'orthographe ou entrer un autre film.")
