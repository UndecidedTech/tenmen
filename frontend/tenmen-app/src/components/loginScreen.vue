<template>
  <div class="hello">
    <label for="name">Username (4 to 8 characters):</label>
    <input type="text" id="username" name="name" required
       minlength="4" maxlength="8" size="10" v-model="user.username">
    <label for="name">Password (4 to 8 characters):</label>
    <input type="text" id="password" name="name" size="10" v-model="user.password" >
    <button class="favorite styled" type="button" size="10" @click="loginClick">
      Login
    </button>
  </div>
</template>
<script>
export default {
  name: 'loginScreen',
  props: {
    msg: String
  },
  methods: {
    loginClick() {
      alert(this.user.username + this.user.password) 
    }
  },
  data() {
    return {
      user:{
        username: "",
        password: ""
      }
      }
  },
}
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
