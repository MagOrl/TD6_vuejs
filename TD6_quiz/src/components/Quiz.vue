<script setup>
import { Quiz } from '../model/quiz.js';

const props = defineProps({
    quiz : Quiz
})
console.log(props.quiz)

</script>

<template>
    <h1>{{ props.quiz.title }}</h1>
</template>