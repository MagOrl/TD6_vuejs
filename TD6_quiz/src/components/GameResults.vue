<script setup>
import { useSelectedQuizStore } from '../stores/selected_quiz';


const store = useSelectedQuizStore();
const results = [];

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