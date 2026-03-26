<script>
import AddQuestion from './AddQuestion.vue'
import DeleteQuestion from './DeleteQuestion.vue'

const url = "http://localhost:5000/questionnaires";
export default {
    components: {
        AddQuestion,
        DeleteQuestion,
    },
    data() {
        return {
            id_quizz: this.$route.params.id,
            quizz_data: {
                questions: null,
            },
        };
    },
    methods: {
        fetchQuizz: async function () {
            const fetched_data = await fetch(url + "/" + this.id_quizz + "/questions", {
                method: "GET",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                },
            }).then((fetched_data) => fetched_data.json());
            this.quizz_data = fetched_data;
            return fetched_data;
        },

        deleteQuestion: async function (num_question) {
            await fetch(url + "/" + this.id_quizz + "/questions/" + num_question, {
                method: "DELETE",
                headers: {
                    Accept: "application/json",
                    "Content-Type": "application/json",
                },
            });
            await this.fetchQuizz();
        },

    },
    mounted() {
        this.fetchQuizz();
    },

};
</script>

<template>
    <section class="questionnaire-layout">
        <div class="questionnaire-main" v-if='quizz_data["questions"] == null || quizz_data["questions"].length == 0'>
            Pas de questions
        </div>
        <div class="questionnaire-main" v-else>
            <ul class="list-group">
                <li class="list-group-item" v-for="(item) in quizz_data['questions']" :key="item.num">
                    <div style="display:flex; justify-content:space-between; align-items:center; gap:1rem;">
                        <span>{{ item.title }}</span>
                        <DeleteQuestion :num="item.num" @delete="deleteQuestion" />
                    </div>
                </li>
            </ul>
        </div>
        <aside class="questionnaire-aside">
            <AddQuestion :id_quizz="parseInt(this.id_quizz)" @added="fetchQuizz" />
        </aside>
    </section>
</template>

<style scoped>
.questionnaire-layout {
    display: grid;
    grid-template-columns: 1fr 280px;
    gap: 1rem;
    align-items: start;
}

.questionnaire-main {
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 1rem;
}

.questionnaire-main li {
    margin-bottom: 0.4rem;
}

.questionnaire-aside {
    border: 1px solid #ddd;
    border-radius: 6px;
    padding: 0.75rem;
}

</style>