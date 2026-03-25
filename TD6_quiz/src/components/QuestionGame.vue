<script setup>
import { useRoute, useRouter } from 'vue-router';

import {Quiz as QuizModel} from '../model/quiz.js';
import { Question as QuestionModel} from '../model/question.js';
import { API_ENDPOINT, QUESTION_ROUTE, QUIZ_ROUTE } from '../constants.js'
import { onBeforeMount, ref } from 'vue';
import QuestionComponent from './QuestionComponent.vue';

const route = useRoute();
const router = useRouter();

let questionIndex = ref(0);
const quiz = ref(null);
const answers = ref([]);
const started = ref(false);

async function fetchQuiz() {
    let response = await fetch(`${API_ENDPOINT}${QUIZ_ROUTE}/${route.params.id}`);

    if(!response.ok){
        return;
    }

    let data = await response.json();

    quiz.value = new QuizModel(
                data.name,
                [],
                data.uri
        );

    response = await fetch(`${API_ENDPOINT}${QUIZ_ROUTE}/${route.params.id}${QUESTION_ROUTE}`);

    if(!response.ok){
        return;
    }

    data = await response.json();

    for(let question_raw of data.questions){
        quiz.value.addQuestion(
            new QuestionModel(
                question_raw.num,
                question_raw.title,
                question_raw.possibilities,
                question_raw.answer
            )
        );
    }
    
}

function saveAnswer(payload){
    answers.value.push(payload.answer);
    nextQuestion();
}

function nextQuestion(){
    console.log(questionIndex.value);
    console.log(getQuestions());
    if(questionIndex.value < (getQuestions().length) -1){
        console.log("next")
        questionIndex.value ++;
    }
    else{
        router.push({
            name: "results"
        })
    }
}

function getQuestions(){
    return JSON.parse(JSON.stringify(quiz.value.questions));
}

onBeforeMount(async () => {
    await fetchQuiz();
})

</script>

<template>
    <div v-if="quiz">
        <h1>{{quiz.title}}</h1>

        <input v-if="!started" type="button" value="Start the Quiz" @click="started = true">
        <QuestionComponent v-else 
            :question="quiz.questions[questionIndex]" 
            @saveAnswer="saveAnswer"
        />
    </div>
    <div v-else>
        <p>Loading quiz ...</p>
    </div>
</template>