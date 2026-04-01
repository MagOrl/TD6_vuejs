# TD6_vuejs
TD6 du rendu en architecture logicelle 

# Lancement

Pour lancer l'api, il faut activer un environement virtuel dans le dossier `/api/` avec la commande : 
```bash
cd api # Si vous êtes dans le dossier racine du projet

python -m venv .venv
source .venv/bin/activate           # & .venv/Script/activate pour windows

pip install -r requirements.txt     # Installer les dépendances
flask syncdb                        # Créer et peupler la BD
flask run                           # Lancer l'API Flask
``` 

Puis dans le dossier `/TD6_quiz` executer la commande :
```bash
cd TD6_quiz     # Si vous êtes dans la dossier racine du projet

npm install     # Installer les dépendances
npm run dev     # Lancer l'application

```



## Jeu de Questionnaires

### Routes 

/quiz :
    Affiche la liste des quizs jouable \

/quizs/:id :
    Affiche le quiz a jouer, avec la possibilité de le commencer.
    Si pas de quiz sélectionné, redirige vers la page des quizs.

/quizs/:id/question/:id :
    Affiche une question du questionnaire sélectionnée.
    Si pas de quiz sélectionné, redirige vers la page des quizs.

/quizs/:id/results : 
    Affiche la page de résultat du quiz actuel
    Si pas de quiz sélectionné, redirige vers la page des quizs.


### Composants

- `QuizList` : fetch et affiche les quizq existant, offrant la possibilité au click d'en sélectionner un, de tenter d'y répondre.

- `QuestionGame` : Affiche le "menu" permettant de démarer le quiz sélectionnée, et de le sélectionner dans le store Pinia.

- `QuestionComponent` : Affiche une question et soit les réponses possible soit un champ de réponse libre, ainsi que la possibilité de passer a la prochaine question, la précédente, et pour la dernière la possibilité de valider le quiz après confirmation.

- `GameResult` : Affiche les résultats du quiz, les bonnes et mauvaises réponses avec les corrections le cas échéant, aisi qu'une note, 1 points par bonne réponse.

### Store

Le store Pinia : useSelectedQuizStore, permet le stockage du quiz sélectionné et des réponses entrées.

Il permet le calcul des points et tient compte de la question actuelle.

