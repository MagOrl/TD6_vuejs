<script>
export default {
    props: {
        quizz: Object,
    },
    methods: {
        fetch: function () {
            this.$emit("fetch");
        }
    },
    emits: ["fetch"]
};
</script>

<template>
    <li>
        <label>
        </label>
    </li>
</template>