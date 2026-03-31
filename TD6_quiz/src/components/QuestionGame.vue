<script setup>
import { useRoute, useRouter } from 'vue-router';
import { useSelectedQuizStore } from '../stores/selected_quiz'

import {Quiz as QuizModel} from '../model/quiz.js';
import { Question as QuestionModel} from '../model/question.js';
import { API_ENDPOINT, QUESTION_ROUTE, QUIZ_ROUTE } from '../constants.js'
import { onBeforeMount } from 'vue';

const router = useRouter();

const store = useSelectedQuizStore();

async function fetchQuiz() {
    let response = await fetch(`${API_ENDPOINT}${QUIZ_ROUTE}/${store.selectedQuiz.id}`);

    if(!response.ok){
        return;
    }

    let data = await response.json();
    let quiz = new QuizModel(
            data.name,
            [],
            data.id
        );

    response = await fetch(`${API_ENDPOINT}${QUIZ_ROUTE}/${store.selectedQuiz.id}${QUESTION_ROUTE}`);

    if(!response.ok){
        return;
    }

    data = await response.json();

    for(let question_raw of data.questions){
        quiz.addQuestion(
            new QuestionModel(
                question_raw.num,
                question_raw.title,
                question_raw.propositions ? question_raw.propositions : [],
                question_raw.answer
            )
        );
    }

    store.setSelectedQuiz(quiz);  
}

function startQuiz(){
    router.push({
        name: "question",
        params : { 
            id :store.selectedQuiz.id, 
            questionIndex : store.currentQuestionIndex}
        }
    )
}

onBeforeMount(async () => {
    await fetchQuiz();
})

</script>

<template>
    <div v-if="store.selectedQuiz">
        <h1>{{store.selectedQuiz.title}}</h1>

        <input type="button" value="Start the Quiz" @click="startQuiz">
    </div>
    <div v-else>
        <p>Loading quiz ...</p>
    </div>
</template>