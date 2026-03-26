<script>
export default {
    props: {
        num: Number,
    },
    methods: {
        del: function () {
            this.$emit('delete', this.num);
        },
    },
    emits: ['delete'],
};
</script>

<template>
    <input type="button" class="btn btn-danger btn-sm" value="supprimer" @click="del" />
</template>
