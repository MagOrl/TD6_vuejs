<script setup>
import { useSelectedQuizStore } from '../stores/selected_quiz';
import { useRouter } from 'vue-router';


const store = useSelectedQuizStore();
const results = [];
const router = useRouter();

for(let resultIndex in store.selectedQuiz.questions){

    const question = store.selectedQuiz.questions[resultIndex];

    const answer = question.possibilities.length > 0 ? question.possibilities[parseInt(store.answers[resultIndex])] : store.answers[resultIndex];
    const solution = question.possibilities.length > 0 ? question.possibilities[question.answer] : question.answer;
    results.push(
        {
            "question" : question.title,
            "answer" : answer,
            "solution" : solution,
            "result" : question.answer == store.answers[resultIndex],
        }
    );
}

function backMenu(){
    router.push({name: "quizs"})
}

</script>

<template>
    <div class="results-container">
        <h1>Results for the Quiz : {{ store.selectedQuiz.title }}</h1>
        <div class="results-list">
            <div 
                v-for="result in results"
                class="result-card"
                :class="result.result ? ' card-correct' : ' card-wrong'"
            >
                <div class="content-container">
                    <p class="question-text">{{ result.question }}</p>

                    <div class="answers-wrapper">
                        <p class="answer-given" :class="result.result ? 'text-success' : 'text-error'">
                            <strong>Answer given:</strong> {{ result.answer || 'No answer' }}
                        </p>
                        <p v-if="!result.result" class="solution-text">
                            <strong>Solution:</strong> {{ result.solution }}
                        </p>
                    </div>
                </div>
            </div>
        </div>

        <div class="score-container">
            <p class="total-score">Total points: <span class="score-value">{{ store.score }}</span></p>
        </div>

        <div>
            <Button @click="backMenu">Retour Menu</Button>
        </div>
    </div>
</template>

<style scoped>
.results-container {
    max-width: 800px;
    margin: 2rem auto;
    padding: 2rem;
    font-family: system-ui, -apple-system, sans-serif;
}

h1 {
    font-size: 1.75rem;
    color: #1a202c;
    text-align: center;
    margin-bottom: 2.5rem;
    font-weight: 700;
}

.quiz-name {
    color: #3b82f6;
}

.results-list {
    display: flex;
    flex-direction: column;
    gap: 1.25rem;
    margin-bottom: 2.5rem;
}

.result-card {
    display: flex;
    padding: 1.5rem;
    border-radius: 12px;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05);
    border-left: 6px solid;
    background-color: #ffffff;
    transition: transform 0.2s;
}

.result-card:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* Correct Answer Styles */
.card-correct {
    border-color: #10b981;
    background-color: #f0fdf4;
}
.text-success {
    color: #059669;
}

/* Wrong Answer Styles */
.card-wrong {
    border-color: #ef4444;
    background-color: #fef2f2;
}
.text-error {
    color: #dc2626;
}

.icon-container {
    font-size: 1.5rem;
    margin-right: 1.25rem;
    display: flex;
    align-items: flex-start;
    padding-top: 0.1rem;
}

.content-container {
    flex: 1;
}

.question-text {
    font-size: 1.15rem;
    font-weight: 600;
    color: #1e293b;
    margin: 0 0 1rem 0;
}

.answers-wrapper {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
    font-size: 0.95rem;
}

.answers-wrapper p {
    margin: 0;
}

.solution-text {
    color: #10b981;
    font-weight: 500;
}

.score-container {
    text-align: center;
    padding: 2rem;
    background-color: #f8fafc;
    border-radius: 12px;
    border: 1px solid #e2e8f0;
}

.total-score {
    font-size: 1.5rem;
    color: #475569;
    font-weight: 600;
    margin: 0;
}

.score-value {
    color: #3b82f6;
    font-size: 2rem;
    font-weight: 700;
    margin-left: 0.5rem;
}
</style>