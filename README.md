# TD6_vuejs
TD6 du rendu en architecture logicelle 

## Sujet

Développer un client web se connectant au serveur REST de quiz permettant de :

- Lister, créer, supprimer et mettre à jour des quiz
- Lister, créer, supprimer et mettre à jour des questions
- Gérer les deux types de questions :
    - Questions à **choix multiples** (réponses proposées)
    - Questions à **réponse libre** (champ texte)

Puis **regrouper** les deux parties dans **une seule application** Vue, avec navigation via **Vue Router** :

- Une partie **jeu** (répondre aux quiz)
- Une partie **édition/admin** (CRUD)

L’accès à la partie édition est **protégé par un mot de passe** (stocké en dur dans le code).

# Lancement

Pour lancer l'API, il faut activer un environnement virtuel dans le dossier `/api/` avec la commande : 
```bash
cd api # Si vous êtes dans le dossier racine du projet

python -m venv .venv
source .venv/bin/activate           # & .venv/Script/activate pour windows

pip install -r requirements.txt     # Installer les dépendances
flask syncdb                        # Créer et peupler la BD
flask run                           # Lancer l'API Flask
``` 

Puis dans le dossier `/TD6_quiz` exécuter la commande :
```bash
cd TD6_quiz     # Si vous êtes dans le dossier racine du projet

npm install     # Installer les dépendances
npm run dev     # Lancer l'application

```

## Application Vue (jeu + édition)

L’application front est dans le dossier `TD6_quiz/`. Elle regroupe :

- **Jeu de questionnaires** : navigation, sélection d’un quiz, enchaînement des questions, page de résultats.
- **Administration/édition** : écrans pour créer / modifier / supprimer quiz et questions.

La navigation est gérée avec **Vue Router** (voir `TD6_quiz/src/routeur.js`).

### Accès à l’administration (mot de passe)

- La page de connexion admin est un composant dédié.
- Le mot de passe est **codé en dur** côté client (conforme au sujet).
- Une fois authentifié, l’utilisateur peut accéder aux écrans de création/mise à jour/suppression.

Note : cette protection est volontairement simple (client-side) car demandée par l’énoncé.



## Jeu de questionnaires

### Routes 

Partie jeu :

- `/quiz` : affiche la liste des quiz jouables.
- `/quizs/:id` : affiche le quiz à jouer, avec la possibilité de le commencer.
    - Si aucun quiz n’est sélectionné, redirige vers `/quiz`.
- `/quizs/:id/question/:id` : affiche une question du quiz sélectionné.
    - Si aucun quiz n’est sélectionné, redirige vers `/quiz`.
- `/quizs/:id/results` : affiche la page de résultat du quiz actuel.
    - Si aucun quiz n’est sélectionné, redirige vers `/quiz`.

Partie administration (protégée) :

- Route de connexion admin (accès par mot de passe).
- Routes d’édition pour le CRUD quiz/questions.

Le détail exact des chemins dépend du routeur (`src/routeur.js`), mais l’application est structurée pour séparer clairement **jeu** et **admin**.


### Composants

#### Jeu

- `QuizList` : récupère et affiche les quiz existants, permet d’en sélectionner un.
- `QuestionGame` : écran d’introduction du quiz sélectionné (démarrer, initialiser le store).
- `QuestionComponent` : affiche une question et :
    - soit des réponses possibles (QCM)
    - soit un champ de réponse libre
    - navigation question précédente/suivante, et validation finale du quiz.
- `GameResults` : affiche les résultats du quiz : bonnes/mauvaises réponses, corrections, et note (1 point par bonne réponse).

#### Administration (CRUD)

- `AdminConnexion` : formulaire de mot de passe et activation de l’accès admin.
- `AddQuizz` / `UpdateQuizz` / `DeleteQuizz` : création, mise à jour et suppression des quiz.
- `AddQuestion` / `DeleteQuestion` : création et suppression des questions (en gérant les deux types).

Les composants “Vue…” (`VueQuizz`, `VueQuestionnaire`) servent de vues/pages pour structurer l’affichage via le routeur.

### Store

Le store Pinia : useSelectedQuizStore, permet le stockage du quiz sélectionné et des réponses entrées.

Il permet le calcul des points et tient compte de la question actuelle.

## API REST (côté serveur)

Le serveur est une API Flask dans `api/`.

- `flask syncdb` initialise et peuple la base.
- Le front consomme l’API via requêtes HTTP (fetch/axios selon l’implémentation).

## Structure du dépôt

- `api/` : serveur Flask (REST)
- `TD6_quiz/` : application Vue (Vite) regroupant jeu + administration


