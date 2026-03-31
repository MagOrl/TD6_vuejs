import {defineStore} from 'pinia';

export const useSelectedQuizStore = defineStore('selectedQuiz', {
    state: () => ({
        selectedQuiz: null,
        answers: [],
        currentQuestionIndex: 0
    }),

    getters : {
        maxQuestionIndex() {
            return this.selectedQuiz ? this.selectedQuiz.questions.length - 1 : 0;
        },
        currentQuestion() {
            return this.selectedQuiz.questions[this.currentQuestionIndex];
        },
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
        }
    }
})