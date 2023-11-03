import { createApp } from 'vue'
import App from './App.vue'
// import Login from './views/login.vue'
import router from "./router"

// createApp(Login).use(router).mount('#app')
createApp(App).use(router).mount('#app')