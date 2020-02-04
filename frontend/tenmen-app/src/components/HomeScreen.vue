<template>
  <div id="app">
    <h1>vue-draw</h1>
    <canvasDraw/>
  </div>
</template>

<script>
import CanvasDraw from '../components/CanvasDraw'

export default {
    name: 'HomeScreen',
    components: {
        CanvasDraw
    }
}
</script>>