<script setup>
import { Question } from '../model/question';
import { ref } from 'vue';


const props = defineProps({
    question : Question
});

const emit = defineEmits({
    saveAnswer: ({answer}) => {
        return true;
    }
});

let answer = ref("");

function saveAnswer(){
    emit('saveAnswer',{answer : answer.value})
    answer.value = "";
}



</script>

<template>
    <div>
        <p>{{ props.question.title }}</p>
        <div v-if="props.question.possibilities === []">
            <input type="text" v-model="answer">
            <input type="button" value="Next" @click="saveAnswer">
        </div>
        <div v-else>
            <div v-for="possibility in props.question.possibilities">
                <input type="radio" :value="possibility" v-model="answer">
            </div>
        </div>
        
    </div>      
</template>