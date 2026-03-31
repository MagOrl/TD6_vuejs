<script setup>
import { ref } from 'vue';
import { useSelectedQuizStore } from "../stores/selected_quiz"
import { router } from '../router/router';

const store = useSelectedQuizStore();

let answer = ref("");

function saveAnswer(){
    store.setAnswer(answer);
    const next = store.nextQuestion();

    router.push({ 
        name: "question",
        params : { 
            id: store.selectedQuiz.id,
            questionIndex : next}
        }
    );

    answer = "";
}

function showResults(){
    store.setAnswer(answer);
    const pursue = confirm("Are you sure you want to finish this Quiz ?")

    pursue ?
    router.push({
        name : "results",
        params : {id : store.selectedQuiz.id} 
    })
    :
    null;
}

</script>

<template>
    <div>
        <p>{{ store.currentQuestion.title }}</p>
        <div v-if="store.currentQuestion.possibilities?.length == 0">
            <input type="text" v-model="answer">
            <input type="button" value="Next" @click="saveAnswer">
        </div>
        <div v-else>
            <div v-for="possibility in store.currentQuestion.possibilities">
                <input type="radio" :value="possibility" v-model="answer">
            </div>
        </div>

        <div>
            <input v-if="store.currentQuestionIndex < store.maxQuestionIndex" type="button" value="Next Question" @click="saveAnswer">
            <input v-else type="button" value="Validate Quiz" @click="showResults"> 
        </div>
        
    </div>      
</template>