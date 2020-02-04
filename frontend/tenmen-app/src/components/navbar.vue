<template>
    <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <a class="navbar-brand" href="#">Tenmen</a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

    <form class="form-inline my-2 my-lg-0">
      <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
      <router-link to="/signup">
        <button class="btn btn-outline-success my-2 my-sm-0" type="submit">Create Account</button>
      </router-link>
    </form>
 
</nav>
</template>
<script>
export default {
    name: "navbar"
}
</script>
<style scoped>

</style>
