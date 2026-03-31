<script setup>
import { useSelectedQuizStore } from '../stores/selected_quiz';


const store = useSelectedQuizStore();
const results = [];

for(let resultIndex in store.selectedQuiz.questions){
    
    const question = store.selectedQuiz.questions[resultIndex];
    results.push(
        {
            "question" : question.title,
            "answer" : store.answers[resultIndex],
            "solution" : question.answer,
            "result" : question.answer == store.answers[resultIndex],
        }
    );
}

</script>

<template>
    <h1>Results for the Quiz : {{ store.selectedQuiz.title }}</h1>

    <div v-for="result in results">
        <p>{{ result.question }}</p>
        <p>Answer given : {{ result.answer }}</p>
        <p>Solution : {{ result.solution }}</p>
    </div>

    <p>Total points : {{ store.score }}</p>
</template>