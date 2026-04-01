<script>
export default {
    props: {
        quizz: Object,
    },
    data() {
        return {
            nom: this.quizz?.name || "",
        };
    },
    methods: {
        update: function () {
            if (this.nom.trim().length !== 0) {
                this.$emit('update', { id: this.quizz.id, name: this.nom });
            }
        },
    },
    emits: ['update'],
};
</script>

<template>
    <div style="display:flex; gap:0.5rem; align-items:center;">
        <input type="text" class="form-control form-control-sm" v-model="nom" placeholder="nouveau nom" />
        <input type="button" class="btn btn-secondary btn-sm" value="renommer" @click="update" />
    </div>
</template>
