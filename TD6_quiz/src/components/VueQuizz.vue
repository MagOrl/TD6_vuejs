<script>
import FetchQuizz from './FetchQuizz.vue'
import AddQuizz from './AddQuizz.vue'

let data = {
  quizz: []
};
const url = "http://localhost:5000/questionnaires";

export default  {
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
    add: async function (nom) {
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
  <div>
    <br>
    <h2> Quizz </h2>
    <FetchQuizz :quizz="this.quizz" @fetch="fetch" @renderQuizz="renderQuizz"/>
    <AddQuizz @add="add" />
  </div>
</template>
