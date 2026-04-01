import {defineStore} from 'pinia';
import { Question } from '../model/question';

export const useSelectedQuizStore = defineStore('selectedQuiz', {
    state: () => ({
        // quiz actuellement sélectionnée
        selectedQuiz: null,

        // la liste des réponses donnée par l'utilisateur 
        // pour le quiz actuel
        answers: [],

        // L'index de la question actuelle
        currentQuestionIndex: 0
    }),

    getters : {
        /**
         * Calcule l'index maximum des questions du quiz
         * @returns {int}
         */
        maxQuestionIndex() {
            return this.selectedQuiz ? this.selectedQuiz.questions.length - 1 : 0;
        },
        /**
         * Récupère la question actuelle a partir de l'index de la question courrante
         * @returns {Question}
         */
        currentQuestion() {
            return this.selectedQuiz.questions[this.currentQuestionIndex];
        },

        /**
         * 
         * @returns Calcule le score selon les réponses fourni
         */
        score() {
            if (!this.selectedQuiz) return 0;
            let correctAnswers = 0;
            this.answers.forEach((answer, index) => {
                if (answer == this.selectedQuiz.questions[index].answer) {
                    correctAnswers++;
                }
            });
            return correctAnswers;
        }

    },

    actions: {
        setSelectedQuiz(quiz) {
            this.selectedQuiz = quiz;
            this.answers = new Array(quiz.questions?.length).fill(null);
            this.currentQuestionIndex = 0;
        },
        setAnswer(answer) {
            this.answers[this.currentQuestionIndex] = answer;
        },
        nextQuestion() {
            if (this.currentQuestionIndex < this.selectedQuiz.questions.length - 1) {
                this.currentQuestionIndex++;
            }

            return this.currentQuestionIndex;
        },
        previousQuestion() {
            if (this.currentQuestionIndex > 0) {
                this.currentQuestionIndex--;
            }

            return this.currentQuestionIndex;
        },

        /**
         * forme une représentation des résultats
         * @returns {Object} la représentation des résultats
         */
        processAnswersResults(){

            const results = [];
            for(let resultIndex in this.selectedQuiz.questions){
                        
                const question = this.selectedQuiz.questions[resultIndex];
                        
                const answer = question.possibilities.length > 0 ? question.possibilities[parseInt(this.answers[resultIndex])] : this.answers[resultIndex];
                const solution = question.possibilities.length > 0 ? question.possibilities[question.answer] : question.answer;
                results.push(
                    {
                        "question" : question.title,
                        "answer" : answer,
                        "solution" : solution,
                        "result" : question.answer == this.answers[resultIndex],
                    }
                );
            }

            return results;
        }
    }
})