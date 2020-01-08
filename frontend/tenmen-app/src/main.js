import Vue from 'vue'
import App from './App.vue'
import Signup from "./Signup.vue"

Vue.config.productionTip = false

Vue.use(VueRouter);

const routes = [
  {path: "/", component: App },
  {path: "/signup", component:  }
]

new Vue({
  render: h => h(App),
}).$mount('#app')
