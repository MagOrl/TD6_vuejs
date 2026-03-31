<script setup>
import { ref } from 'vue';
import { useSelectedQuizStore } from "../stores/selected_quiz"
import { router } from '../router/router';

const store = useSelectedQuizStore();

const answer = ref("");

function saveAnswer(){
    store.setAnswer(answer.value);
    const next = store.nextQuestion();

    router.push({ 
        name: "question",
        params : { 
            id: store.selectedQuiz.id,
            questionIndex : next}
        }
    );

    answer.value = "";
}

function showResults(){
    store.setAnswer(answer.value);
    const pursue = confirm("Are you sure you want to finish this Quiz ?")

    pursue ?
    router.push({
        name : "results",
        params : {id : store.selectedQuiz.id} 
    })
    :
    null;
}

function backQuestion(){
    const previous = store.previousQuestion();
    router.push({ 
        name: "question",
        params : { 
            id: store.selectedQuiz.id,
            questionIndex : previous}
        }
    );
}

</script>

<template>
    <div>
        <p>{{ store.currentQuestion.title }}</p>
        <div v-if="store.currentQuestion.possibilities?.length == 0">
            <input type="text" v-model="answer">
        </div>
        <div v-else>
            <fieldset>
                <legend>Possibilitées</legend>
                <div v-for="possibility in store.currentQuestion.possibilities">
                    <input type="radio" :id="possibility" :value="store.currentQuestion.possibilities.indexOf(possibility)" v-model="answer" >
                    <label :for="possibility">{{ possibility }}</label>
                </div>
            </fieldset>
        </div>

        <div>
            <input v-if="store.currentQuestionIndex > 0" type="button" value="Previous Question" @click="backQuestion"> 

            <input v-if="store.currentQuestionIndex < store.maxQuestionIndex" type="button" value="Next Question" @click="saveAnswer">
            <input v-else type="button" value="Validate Quiz" @click="showResults"> 
        </div>
        
    </div>      
</template>