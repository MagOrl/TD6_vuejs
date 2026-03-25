import { createWebHistory, createRouter } from "vue-router";

import VueQuizz from "./components/VueQuizz.vue";
import VueQuestionnaire from "./components/VueQuestionnaire.vue";

const routes = [
  { path: "/", component: VueQuizz },
  { path: "/quizz", component: VueQuizz },
  { path: "/quizz/:id", component: VueQuestionnaire },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
