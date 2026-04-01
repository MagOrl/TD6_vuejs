<script>
export default {
    props: {
        id: Number,
    },
    methods: {
        del: function () {
            this.$emit('delete', this.id);
        },
    },
    emits: ['delete'],
};
</script>

<template>
    <input type="button" class="btn btn-danger btn-sm" value="supprimer" @click="del" />
</template>
