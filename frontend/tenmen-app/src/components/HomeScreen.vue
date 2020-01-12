<template>
  <div id="app">
    <h1>vue-draw</h1>
    <div class="show-area">
      <CanvasDraw :width="640" :height="480" :outputName="'example'"/>
    </div>
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