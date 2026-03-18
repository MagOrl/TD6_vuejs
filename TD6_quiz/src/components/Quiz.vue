<script setup>
import { Quiz } from '../model/quiz.js';
import { useRouter } from 'vue-router';

const router = useRouter();

const props = defineProps({
    quiz : Quiz
})

function openQuiz(){
    console.log("opening quiz");
    router.push({
        name: "game",
        params : {id : props.quiz.url.split('/').at(-1)}
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
