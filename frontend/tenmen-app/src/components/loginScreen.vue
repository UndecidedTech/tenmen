<template>
<div>
  <img class="pepe" height="140px" src="../assets/pepe.png"/>
  <div class="row">
   <body class="text-center mx-auto">
    <form class="form-signin">
    <img class="mb-4" src="/docs/4.4/assets/brand/bootstrap-solid.svg" alt="" width="72" height="72">
    <h1 class="h3 mb-3 font-weight-normal">Please log in</h1>
    <label for="inputUsername" class="sr-only">Username</label>
    <input type="username" id="inputUsername" class="form-control" placeholder="Username" required="" autofocus="" v-model="user.username">
    <label for="inputPassword" class="sr-only">Password</label>
    <input type="password" id="inputPassword" class="form-control" placeholder="Password" required="" v-model="user.password">
    <div class="checkbox mb-3">
        <label>
            <input type="checkbox" value="remember-me"> Remember me
        </label>
  </div>
  <button class="btn btn-lg btn-primary btn-block" @click="loginClick">Log in</button>
</form>


</body>
  </div>
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
.pepe {
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>
