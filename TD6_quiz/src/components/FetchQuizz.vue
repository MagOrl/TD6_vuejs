<script>
export default {
    methods: {
        fetch: function () { this.$emit('fetch'); 
        }
    },
    props: {
        quizz: Object,
    },
    emits:["fetch"],
};
</script>

<template>
    <input type="button" class="btn btn-info" @click="fetch" value="refresh">
    <li v-for="(item) in quizz">
        <label>
            {{ item.name }}
        </label>
    </li>
</template>