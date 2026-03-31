<script>
export default {
    data() {
            return {
              nom: "",
            };
          },
    methods:{
       add: function(){
            if(this.nom.trim().length!=0)
                this.$emit('add', this.nom )
                this.nom ="";
              },
    },
    emits:["add"]
};
</script>
<template>
<input type="text" placeholder="nouvelle question" v-model="nom">
<input type="button" class="btn btn-info" value="ajouter" @click="add"/>
</template>