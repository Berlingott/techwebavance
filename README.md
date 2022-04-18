# TechWebAvancee

Trouver le projet sur https://github.com/empoi1/TechWebAvancee

* Simon Duchesne
* Emery poirier

Devoir 1 du cours  8INF349 - Technologies Web avancées
Création d'un blog à l'aide de Flask.

=============================================
# Instruction spécifiques

Les utilisateur suivant sont créés de base à des fins de tests


Utilisateur/mot de passe: admin / admin

Cet utilisateurs détiens les droits d'administrateur

Utilisateur/mot de passe: autheur / admin
 
Cet utilisateurs détiens les droits d'autheur


Utilisateur/mot de passe: simon / admin

Cet utilisateur est un lecteur

==============================================================
# Devoir
L'objectif du projet de session est de développer et déployer Nous allons développer un blog Web.
Le projet est divisé en deux étapes pour chacune des remises.
# Objectifs
• Se familiariser avec le développement Web
• Développer une application Web
• Développer une API REST (pour la partie 2)
• S'assurer de la résilience et de la performance d'une application Web (pour la partie 2)
• Déployer une application Web (pour la partie 2)
# Contexte
Son équipe a été embauchée pour développer le blog technique de SpotiNyk, une société qui
développe une application du même nom pour diffuser de la musique. Le client pense que la
publication d'articles techniques sur son logiciel ajouterait de la valeur au produit car cela inspirerait
confiance aux autres professionnels de l'ingénierie logicielle.
Ainsi, le client souhaite que vous construisiez un blog Web avec une mise en page propre et
cohérente et avec les caractéristiques suivantes :
Vous devez créer une application de blog Web, stockant les articles, les commentaires et les balises
(tags) dans une base de données. Vous devez créer des sessions pour connecter les utilisateurs afin
qu'ils rédigent des commentaires. Vous devez valider la soumission des données via des formulaires.
Vous devez créer un ensemble clair et complet de modèles de pages HTML pour l'application. Vous
devez créer un panneau d'administration qui vous permet de créer de nouveaux articles ou de
modifier des articles existants. Créez également une API RESTFUL qui permet la saisie de
commentaires via Ajax et enfin, créer un ensemble de tests unitaires pour s'assurer que l'application
fonctionne.
# Exigences de l'application
1) N'importe qui peut s'inscrire en tant que lecteur.
2) Seul un administrateur peut modifier le profil d'un autre utilisateur.
3) Un lecteur peut commenter un article,
4) Un lecteur peut réagir à un article (aimer ou applaudir)
5) Un auteur peut publier un article
6) Un auteur peut réviser (éditer) un article
7) Un auteur peut supprimer un article
8) Un auteur peut changer le statut d'un article (publié ou brouillon)
9) Tous les articles publiés sont publics et l'utilisateur n'a pas besoin d'être connecté pour les lire.
10) Les commentaires et réactions à un article nécessitent une authentification.
Remarque : dans la première livraison du projet, la fonctionnalité de commentaire ou de réaction à
un article n'a pas besoin d'être asynchrone, c'est-à-dire que l'utilisation d'Ajax ne sera pas requise.
Relation d’entité
Livrable
Sur le site Moodle du cours, remettez:
1) Un fichier compressé de votre projet, contenant :
- tous vos fichiers de projet,
- un fichier de configuration (config.py),
- un fichier de configuration requise pour l'installation (requirements.txt).
Noter: Le fichier compressé ne doit pas contenir : les fichiers de cache python, le dossier
d'environnement (env).
2) Un fichier avec les noms des membres de l'équipe. Si nécessaire, dans ce même fichier, vous
pouvez ajouter d'éventuelles instructions supplémentaires pour faire fonctionner votre projet.