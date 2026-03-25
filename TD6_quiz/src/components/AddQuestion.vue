<script>
export default {
    data() {
        return {
            nom: "",
        };
    },
    methods: {
        add: async function (nom, type) {
            await fetch(url, {
                method: "POST",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    name: nom,
                }),
            });
        },
    },
};
</script>
<template>
    <form class="question-form">
        <h3>Ajouter une question</h3>
        <label for="question-name">Intitulé</label>
        <input id="question-name" type="text" placeholder="nouvelle question" v-model="nom">

        <select id="list">
            <option value="Ouverte"> Ouverte</option>
            <option value="Fermé"> Fermé </option>
        </select>
        <input type="button" class="question-form-btn" value="ajouter" @click="add" />
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