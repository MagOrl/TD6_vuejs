<script>
import AddQuizz from './AddQuizz.vue'
import DeleteQuizz from './DeleteQuizz.vue'
import UpdateQuizz from './UpdateQuizz.vue'

let data = {
  quizz: []
};
const url = "http://localhost:5000/questionnaires";

export default  {
  components: {
    AddQuizz,
    DeleteQuizz,
    UpdateQuizz,
  },
  data() {
    return data;
  },
  mounted() {
    this.fetch();
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
      await this.fetch();
    },
    deleteQuiz: async function (id) {
      await fetch(url + "/" + id, {
        method: "DELETE",
        headers: {
          Accept: "application/json",
        },
      });
      await this.fetch();
    },
    updateQuiz: async function (payload) {
      await fetch(url + "/" + payload.id, {
        method: "PUT",
        headers: {
          Accept: "application/json",
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          name: payload.name,
        }),
      });
      await this.fetch();
    },
  },
};

</script>

<template>
  <div>
    <br>
    <h2> Quizz </h2>
    <AddQuizz @add="add" />

    <ul class="list-group" style="margin-top: 0.75rem;">
      <li class="list-group-item" v-for="(item) in quizz" :key="item.id">
        <div style="display:flex; justify-content:space-between; gap:1rem; align-items:center;">
          <div>
            <label style="cursor:pointer;" @click="$router.push('/quizz/' + item.id)">
              {{ item.name }}
            </label>
          </div>
          <div style="display:flex; gap:0.5rem; align-items:center;">
            <UpdateQuizz :quizz="item" @update="updateQuiz" />
            <DeleteQuizz :id="item.id" @delete="deleteQuiz" />
          </div>
        </div>
      </li>
    </ul>
  </div>
</template>
