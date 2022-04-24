# TechWebAvancee

Trouver le projet sur https://github.com/empoi1/TechWebAvancee

* Simon Duchesne
* Emery poirier

Devoir 2 du cours  8INF349 - Technologies Web avancées

=============================================
# Compilation
Veuillez faire les commandes suivantes lorsque votre logicielle Docker est ouvert:

* docker-compose build
* docker-compose up

Veuillez effectué ces commandes dans le dossier TechWebAv ou se trouvent les fichiers requirements.txt, Dockerfile et docker-compose.yml

=============================================
# Utilisation

Une fois le docker lancé, veuillez utiliser l'adresse suivante pour accèder au site web.
* http://localhost:8000/

=============================================
#API

Voici les lien et les méthodes pour l'utilisation de l'API:

Méthode lister tous les articles 
* GET - http://localhost:8000/api/article/

Méthode pour lister un article
* GET - http://localhost:8000/api/article/<article_id>

Méthode pour Créer une article
* PUT - http://localhost:8000/api/article/

d) Méthode pour modifier une article
* POST - http://localhost:8000/api/article/

Méthode supprimer l'article
* DELETE - http://localhost:8000/api/article/1



=============================================
# Comptes utilisable

Les utilisateur suivant sont créés de base à des fins de tests

Sous la forme rôle: Utilisateur/mot de passe

* Admin : admin / admin
* auteur: autheur / admin
* Utilisateur: simon / admin

=============================================