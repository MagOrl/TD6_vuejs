<script setup>
import { useRoute } from 'vue-router';

import {Quiz as QuizModel} from '../model/quiz.js';
import {Question as QuestionModel} from '../model/question.js';
import { API_ENDPOINT, QUESTION_ROUTE, QUIZ_ROUTE } from '../constants.js'
import { onBeforeMount, ref } from 'vue';

const route = useRoute();

const questionIndex = ref(0);
const quiz = ref(null);
const answers = ref([]);

async function fetchQuestions() {
    const response = await fetch(`${API_ENDPOINT}${QUIZ_ROUTE}/${route.params.id}`);

    if(!response.ok){
        return;
    }

    const data = await response.json();

    console.log(data);
}

onBeforeMount(async () => {
    await fetchQuestions();
})

</script>

<template>
    <h1>Some text</h1>

</template>