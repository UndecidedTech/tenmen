<template>
<div>
    <div class="container">
    <div class="row">
        <div class="form-group col-6">
            <label for="inputUsername">Username:</label>
            <input type="text" class="form-control" id="inputUsername"/>
        </div>    
        <div class="form-group col-6">
            <label for="inputPassword">Password:</label>
            <input type="text" class="form-control" id="inputPassword"/>
        </div>
    </div>
    </div>
</div>
</template>
<script>
export default {
  name: 'signupScreen',
  data() {
    return {
      user: {
            username: "",
            password: "",
            first_name: "",
            last_name: "",
            email: ""
        }
      }
  }
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
.container {
    position: relative;
    width: 80%;
    height: 100%

}
</style>
