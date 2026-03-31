import { createWebHistory, createRouter } from "vue-router";

import Home from "./components/Home.vue";
import QuizList from "./components/QuizList.vue";
import QuestionGame from "./components/QuestionGame.vue";
import Question from "./components/QuestionComponent.vue";
import GameResults from "./components/GameResults.vue";
import VueQuizz from "./components/VueQuizz.vue";
import VueQuestionnaire from "./components/VueQuestionnaire.vue";

const routes = [
  { path: "/", alias:["/home","/about"],component: Home },
  { path: "/quizz", name: "VueQuizz", component: VueQuizz },
  { path: "/quizz/:id", component: VueQuestionnaire },
  {
    path: "/quiz",
    name: "quizs",
    alias: "/quiz",
    component: QuizList,
  },
  {
    path: "/quizs/:id(\\d+)",
    alias: "/:id(\\d+)",
    name: "game",
    component: QuestionGame,
  },
  {
    path: "/quizs/:id(\\d+)/question/:questionIndex(\\d+)",
    name: "question",
    component: Question,
  },
  {
    path: "/quizs/:id(\\d+)/results",
    name: "results",
    component: GameResults,
  },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});
