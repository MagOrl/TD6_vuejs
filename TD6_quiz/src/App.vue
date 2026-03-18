<script>
import FetchQuizz from './components/FetchQuizz.vue'
import AddQuizz from './components/AddQuizz.vue'

let data = {
  quizz: []
};
const url = "http://localhost:5000/questionnaires";

export default {
  components: {
    FetchQuizz,
    AddQuizz,
  },
  data() {
    return data;
  },
  methods: {
    fetch: async function () {
      const fetched_data = await fetch(url, {
        method: "GET",
        headers: {
          Accept: "application/json",
        },
      }).then((fetched_data) => fetched_data.json());
      this.quizz = fetched_data["questionnaires"];
      
    },
    add:async function(nom){
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
    }
  },
};

</script>

<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <div>
    <br>
    <h2> Quizz </h2>
    <FetchQuizz :quizz="this.quizz" @fetch="fetch" />
    <AddQuizz @add="add" />
  </div>
</template>
