                                                 ![Getting Started](img/oc_lettings_logo_dark.png)

## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


## **CI/CD (Intégration continue et déploiement continu)**
 ### **Conditions préalables**
  - Python 3.9.x ou supérieur
  - Docker pour la conteneurisation
  - CircleCI pour l'intégration/le développement continu
  - Sentry pour le suivi des erreurs
  - Heroku pour le déploiement

 ### **Développement local depuis Dockerhub**

  Pour exécuter l'application localement à l'aide de Docker, procédez comme suit :

  - Téléchargez et installez docker.
  - Construisez votre image docker avec : `docker build -t image .`
  - Exécutez un conteneur docker avec : `docker run -d --name your-container-name -p 8000:8000 your-image-name`

  Il est également possible d'utiliser docker pull pour extraire l'image pré-construite de Dockerhub à l'aide de la commande suivante :
  docker pull <nom-image>
  Pour ce projet, l'image Docker est disponible sur `docker pull oc_lettings`
  Après avoir extrait l'image, vous pouvez exécuter le conteneur à l'aide de la commande suivante :
  `docker run -d --name oc_lettings -p 8000:8000 oc_lettings`.

  Accédez à http://localhost:8000 dans votre navigateur Web pour accéder à l'application

  ### **CercleCI**
  Ce projet utilise CircleCI pour l'intégration continue.
  La configuration de CircleCI se trouve dans le fichier `.circleci/config.yml`.

  #### **Pour configurer CircleCI pour votre propre projet, suivez ces étapes :**

  Créez un compte CircleCI et connectez votre compte GitHub
  Créez un nouveau projet et sélectionnez votre répositoire GitHub
  Ajoutez les variables d'environnement requises aux paramètres du projet CircleCI :
  **DOCKER_USERNAME** : votre nom d'utilisateur Docker Hub
  **DOCKER_LOGIN** : Votre e-mail de connexion Docker Hub
  **HEROKU_APP_NAME** : le nom de votre application Heroku
  **HEROKU_TOKEN** : Votre clé API Heroku
  Poussez un nouveau commit vers votre répositoire pour déclencher un nouveau build sur CircleCI

  ### **Sentry**
  Ce projet utilise Sentry pour le suivi des erreurs. La configuration de Sentry se trouve dans le fichier settings.py.

  #### **Pour configurer Sentry pour votre propre projet, procédez comme suit :**

  Créez un compte Sentry et créez un nouveau projet

  Ajoutez la variable d'environnement SENTRY_DSN au fichier .env de votre projet

  Installez le package Python sentry-sdk : `pip install sentry-sdk`

  Ajoutez le code généré au fichier settings.py 

  ### **Déploiement sur Heroku**

  #### **Pour déployer l'application sur Heroku, procédez comme suit :**

  - Créer une nouvelle application `Heroku` dans le tableau de bord Heroku

  - Ajoutez les variables d'environnement **DATABASE_URL** et **SECRET_KEY** aux paramètres de votre application

  - Ajoutez la remote Heroku Git à votre répositoire local : heroku git:remote -a your-heroku-app-name

  - Poussez l'application vers Heroku à l'aide du registre de conteneurs Heroku :

  conteneur heroku : `connexion`

  conteneur heroku : `push -a web nom-de-l-application-heroku`

  conteneur heroku : `release -a web nom-de-l-application-heroku`

  Votre application devrait maintenant être déployée et accessible sur https://your-heroku-app-name.herokuapp.com

### **Auteurs**

  - **`Openclassrooms`**
  - **`Gavin Humphrey`**

