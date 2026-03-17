<script>
import FetchQuizz from './components/FetchQuizz.vue'

let data = {
  quizz: []
};
const url = "http://localhost:5000/questionnaires";

export default {
  components: {
    FetchQuizz,
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
      this.quizz.push(fetched_data);
      console.log(this.quizz[0]);
    },
  },
};

</script>

<template>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css"
    integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
  <div>
    <h2> Quizz </h2>
    <FetchQuizz v-for="(item, index) in quizz" :key="item.text" />

<input type="button" class="btn" @click="fetch" value="refresh">

  </div>
</template>
