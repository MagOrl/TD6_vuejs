<script>
const url = "http://localhost:5000/questionnaires";

export default {
    data() {
        return {
            nom: "",
            type_question: "ouverte",
            answer: "",
            answer_fermee: "",
            answer_fermee_real: "",
        };
    },
    methods: {
        add: async function (nom, type_question, answer, id_quizz, answer_fermee, answer_fermee_real) {
            if (this.type_question == "ouverte") {
                await fetch(url + "/" + id_quizz + "/questions", {
                    method: "POST",
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        title: nom,
                        type: type_question,
                        answer: answer,
                    }),
                });
            } else {
                await fetch(url + "/" + id_quizz + "/questions", {
                    method: "POST",
                    headers: {
                        Accept: "application/json",
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        title: nom,
                        type: type_question,
                        answer: answer_fermee_real,
                        proposition1: answer_fermee_real,
                        proposition2: answer_fermee,
                    }),
                });
            }
        },

    },
    props: {
        id_quizz: Number
    }

}
</script>
<template>
    <form class="question-form">
        <h3>Ajouter une question</h3>
        <label for="question-name">Intitulé</label>
        <input id="question-name" type="text" placeholder="nouvelle question" v-model="nom">

        <select id="list" v-model="type_question">
            <option value="ouverte"> Ouverte</option>
            <option value="fermee"> Fermé </option>
        </select>
        <div v-if='type_question == "ouverte"'>
            <input id="question-name" type="text" placeholder="mettre la bonne réponse" v-model="answer">
        </div>
        <div v-else>
            <input id="question-name" type="text" placeholder="mettre la mauvaise réponse" v-model="answer_fermee">
            <input id="question-name" type="text" placeholder="mettre la bonne réponse" v-model="answer_fermee_real">
        </div>

        <input type="button" class="question-form-btn" value="ajouter"
            @click="add(nom, type_question, answer, id_quizz, answer_fermee, answer_fermee)" />
    </form>
</template>

<style scoped>
.question-form {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.question-form h3 {
    margin: 0 0 0.25rem 0;
    font-size: 1rem;
}

.question-form label {
    font-size: 0.9rem;
}

.question-form input[type="text"] {
    padding: 0.45rem 0.6rem;
    border: 1px solid #ccc;
    border-radius: 4px;
}

.question-form-btn {
    margin-top: 0.25rem;
    padding: 0.45rem 0.7rem;
    border: 1px solid #bbb;
    border-radius: 4px;
    background: #328adb;
    cursor: pointer;
}
</style>