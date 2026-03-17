<script setup>

import { ref, onMounted } from 'vue';
import Quiz from './Quiz.vue';
import {Quiz as QuizModel} from '../model/quiz.js';
import {Question as QuestionModel} from '../model/question.js';
import { API_ENDPOINT, QUESTION_ROUTE, QUIZ_ROUTE } from '../constants.js'

const quizs = ref([]);

async function fetchQuizs(){

    const response = await fetch(`${API_ENDPOINT}${QUIZ_ROUTE}`);

    if(!response.ok){
        return;
    }

    const data = await response.json();

    console.log(data);

    for(let quiz in data){

        quizs.value.push(
            new QuizModel(
                quiz["name"],
                null,
                null,
                quiz["uri"]
            )
        )
    }
}

onMounted( 
  async() => await fetchQuizs()
);

</script>

<template>
    <div v-for="quiz in quizs">
        <Quiz :quiz="quiz" />
    </div>
</template>