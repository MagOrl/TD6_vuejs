# TD6_vuejs

TD6 du rendu en architecture logicielle.

## Sujet

Développer un client web se connectant au serveur REST de quiz, permettant de :

- Lister, créer, supprimer et mettre à jour des quiz
- Lister, créer, supprimer et mettre à jour des questions
- Gérer **les deux types de questions** :
    - **Question ouverte** : réponse libre (champ texte)
    - **Question fermée** : choix multiples (propositions)

Puis **regrouper** les deux parties dans **une seule application** Vue, avec navigation via **Vue Router** :

- Une partie **jeu** (répondre aux quiz)
- Une partie **édition/admin** (CRUD)

L’accès à la partie édition est **protégé par un mot de passe** (stocké en dur dans le code).

## Lancement

### API (Flask)

Depuis la racine du projet :

```bash
cd api

python -m venv .venv
source .venv/bin/activate           # Windows: .venv/Scripts/activate

pip install -r requirements.txt
flask syncdb                        # Crée et peuple la BD
flask run                           # Lance l'API Flask
```

### Front (Vue + Vite)

Dans un autre terminal, depuis la racine :

```bash
cd TD6_quiz
npm install
npm run dev
```

## Architecture (1 application = jeu + admin)

L’application front est dans `TD6_quiz/`.

- La navigation est gérée par Vue Router : `TD6_quiz/src/routeur.js`
- L’application est structurée en composants (dossier `TD6_quiz/src/components/`)

## Routes (Vue Router)

### Partie jeu

- `/quiz` : liste des quiz jouables.
- `/quizs/:id` : écran de démarrage du quiz sélectionné.
- `/quizs/:id/question/:questionIndex` : affiche une question du quiz.
- `/quizs/:id/results` : affiche la page de résultats.

### Partie administration (protégée)

- `/connexion` : page de connexion admin.
- `/quizz` : administration des quiz (CRUD).
- `/quizz/:id` : administration des questions d’un quiz (ajout/suppression).

## Composants principaux

### Jeu

- `QuizList` : récupère et affiche les quiz, permet d’en sélectionner un.
- `QuestionGame` : écran d’introduction du quiz sélectionné (démarrer, init store).
- `QuestionComponent` : affiche une question et :
    - soit des propositions (question fermée)
    - soit un champ de réponse (question ouverte)
    + navigation et validation du quiz.
- `GameResults` : affiche les résultats (bonnes/mauvaises réponses, corrections, note).

### Administration (CRUD)

- `AdminConnexion` : authentification par identifiants **en dur**.
- `VueQuizz` : vue/page d’admin des quiz.
    - `AddQuizz`, `UpdateQuizz`, `DeleteQuizz`
- `VueQuestionnaire` : vue/page d’admin des questions d’un quiz.
    - `AddQuestion`, `DeleteQuestion`

## Store (Pinia)

Le store `useSelectedQuizStore` (dossier `TD6_quiz/src/stores/`) stocke le quiz sélectionné et les réponses de l’utilisateur.
Il permet notamment le calcul des points et la gestion de la question courante.

## API REST (serveur)

Le serveur est une API Flask dans `api/`.
Le front consomme l’API via requêtes HTTP (fetch) (ex : endpoints de questionnaires et questions).

## Structure du dépôt

- `api/` : serveur Flask (REST)
- `TD6_quiz/` : application Vue (Vite) regroupant jeu + administration

