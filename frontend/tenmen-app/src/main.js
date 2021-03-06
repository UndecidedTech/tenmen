import Vue from 'vue'
import App from './App.vue'
import VueRouter from "vue-router"
import signupScreen from "./components/signupScreen"
import loginScreen from "./components/loginScreen"
import HomeScreen from "./components/HomeScreen"
Vue.config.productionTip = false

Vue.use(VueRouter);

const routes = [
  {path: "/", component: loginScreen},
  {path: "/signup", component: signupScreen},
  {path: "/home", component: HomeScreen}
]

const router = new VueRouter({
  routes
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
