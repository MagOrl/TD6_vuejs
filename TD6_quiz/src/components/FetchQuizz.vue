<script>

export default {
    methods: {
        fetch: function () {
            this.$emit('fetch');
        },
        goToQuestionnaire: function (quizz) { this.$router.push('/quizz/' + quizz.id); },
    },
    props: {
        quizz: Object,
    },
    emits: ["fetch"],
};
</script>

<template>
    <input type="button" class="btn btn-info" @click="fetch" value="refresh">
    <li v-for="(item) in quizz">
        <label @click="goToQuestionnaire(item)">
            {{ item.name }}
        </label>
    </li>
</template>