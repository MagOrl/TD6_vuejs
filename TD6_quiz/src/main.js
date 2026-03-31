import { createApp } from 'vue'
import './style.css'
import {router} from './routeur.js'
import App from './App.vue'

import { router } from './router/router.js'
import { createPinia } from 'pinia'

const pinia = createPinia()
createApp(App).use(pinia).use(router).mount('#app')
