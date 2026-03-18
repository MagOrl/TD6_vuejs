import { createMemoryHistory, createRouter } from 'vue-router';

import QuizList from '../components/QuizList.vue';
import QuestionGame from '../components/QuestionGame.vue';

const routes = [
    {
        path: '/',
        name : "quizs",
        alias : "/quiz",
        component: QuizList,
    },
    {
        path : '/quizs/:id(\\d+)',
        alias : '/:id(\\d+)',
        name : "game",
        component : QuestionGame
    }
] 

export const router = createRouter({
    history : createMemoryHistory(),
    routes
});