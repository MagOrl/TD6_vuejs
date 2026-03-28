<script setup>
import { Quiz } from '../model/quiz.js';
import { useRouter } from 'vue-router';
import { useSelectedQuizStore } from '../stores/selected_quiz.js';

const router = useRouter();

const props = defineProps({
    quiz : Quiz
})

const store = useSelectedQuizStore();

function openQuiz(){
    store.setSelectedQuiz(props.quiz);
    router.push({
        name: "game",
        params : {id : props.quiz.id}
    });
}

</script>

<template>
    <div @click="openQuiz">
        <h1>{{ props.quiz.title }}</h1>
    </div>
</template>

<style scoped>
div{
    background-color: aqua;
    padding-left : 50px;
    padding-right : 50px;
}
</style>
