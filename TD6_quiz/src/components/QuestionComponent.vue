<script setup>
import { ref } from 'vue';
import { useSelectedQuizStore } from "../stores/selected_quiz"
import { useRouter } from 'vue-router';

const store = useSelectedQuizStore();
const router = useRouter();
const answer = ref("");

function saveAnswer(){
    store.setAnswer(answer.value);
    const next = store.nextQuestion();

    router.push({ 
        name: "question",
        params : { 
            id: store.selectedQuiz.id,
            questionIndex : next}
        }
    );

    answer.value = "";
}

function showResults(){
    store.setAnswer(answer.value);
    const pursue = confirm("Are you sure you want to finish this Quiz ?")

    pursue ?
    router.push({
        name : "results",
        params : {id : store.selectedQuiz.id} 
    })
    :
    null;
}

function backQuestion(){
    const previous = store.previousQuestion();
    router.push({ 
        name: "question",
        params : { 
            id: store.selectedQuiz.id,
            questionIndex : previous}
        }
    );
}

function backMenu(){
    router.push({name: "quizs"});
}

</script>

<template>
    <div>
        <button class="give-up" @click="backMenu">Give up</button>
    </div>

    <div class="question-container">
        <p class="question-title">{{ store.currentQuestion.title }}</p>
        <div v-if="store.currentQuestion.possibilities?.length == 0">
            <input type="text" class="input-text" v-model="answer">
        </div>
        <div v-else>
            <fieldset>
                <legend>Possibilitées</legend>
                <div v-for="possibility in store.currentQuestion.possibilities" class="radio-option">
                    <input type="radio" :id="possibility" :value="store.currentQuestion.possibilities.indexOf(possibility)" v-model="answer" :checked="store.currentQuestion.possibilities.indexOf(possibility) == 0">
                    <label :for="possibility">{{ possibility }}</label>
                </div>
            </fieldset>
        </div>

        <div class="button-group">
            <input 
                v-if="store.currentQuestionIndex > 0" 
                class="btn btn-secondary" 
                type="button" 
                value="Previous Question" 
                @click="backQuestion"
            > 
            <input 
                v-if="store.currentQuestionIndex < store.maxQuestionIndex" 
                class="btn btn-primary" 
                type="button" 
                value="Next Question" 
                @click="saveAnswer"
            >
            <input 
                v-else 
                class="btn btn-validate" 
                type="button" 
                value="Validate Quiz" 
                @click="showResults"
            > 
        </div>
        
    </div>      
</template>

<style scoped>
.question-container {
    max-width: 600px;
    margin: 2rem auto;
    padding: 2rem;
    border: 1px solid #e2e8f0;
    border-radius: 12px;
    background-color: #ffffff;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    font-family: system-ui, -apple-system, sans-serif;
}

.question-title {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1a202c;
    margin-bottom: 1.5rem;
}

.input-text {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #cbd5e1;
    border-radius: 6px;
    font-size: 1rem;
    box-sizing: border-box;
    transition: border-color 0.2s;
}

.input-text:focus {
    outline: none;
    border-color: #3b82f6;
    box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1);
}

fieldset {
    border: 1px solid #e2e8f0;
    border-radius: 8px;
    padding: 1.25rem;
    margin-bottom: 1.5rem;
    background-color: #f8fafc;
}

legend {
    font-weight: 600;
    color: #475569;
    padding: 0 0.5rem;
}

.radio-option {
    margin-bottom: 0.75rem;
    display: flex;
    align-items: center;
}

.radio-option:last-child {
    margin-bottom: 0;
}

.radio-option input[type="radio"] {
    margin-right: 0.75rem;
    cursor: pointer;
    width: 16px;
    height: 16px;
}

.radio-option label {
    cursor: pointer;
    color: #334155;
}

.button-group {
    display: flex;
    justify-content: space-between;
    margin-top: 2rem;
}

.btn {
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 6px;
    font-size: 1rem;
    font-weight: 500;
    cursor: pointer;
    transition: background-color 0.2s, transform 0.1s;
}

.btn:active {
    transform: translateY(1px);
}

.btn-primary {
    background-color: #3b82f6;
    color: white;
    margin-left: auto; /* Pushes the next button to the right if there is no previous button */
}

.btn-primary:hover {
    background-color: #2563eb;
}

.btn-secondary {
    background-color: #e2e8f0;
    color: #475569;
}

.btn-secondary:hover {
    background-color: #cbd5e1;
}

.btn-validate {
    background-color: #10b981;
    color: white;
    margin-left: auto;
}

.btn-validate:hover {
    background-color: #059669;
}

.give-up {
    background-color: red;
}
</style>