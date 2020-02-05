<template>
  <div id="sketch-holder">
  </div>
</template>

<script>
import io from "socket.io-client"
import p5 from "p5"

export default {
  name: 'CanvasDraw',
  mounted() {
    this.setupCanvas();
  },
  data() {
    return {
      socket: io('http://localhost:5000')
    }
  },
  
  methods: {
    setupCanvas(){
    var canvas = p5.createCanvas(600,400);
    canvas.parent("sketch-holder")
    p5.background(51);

    this.socket.on('mouse', this.newDrawing);
    },
    mouseDragged() {
    var data = {
        x: p5.mouseX,
        y: p5.mouseY
    }
    this.socket.emit('mouse' , data);
    p5.noStroke();
    p5.fill(255);
    p5.ellipse(p5.mouseX, p5.mouseY, 36,36);
    },
    newDrawing(data){
    p5.noStroke();
    p5.fill(255 , 0 , 100);
    p5.ellipse(data.x, data.y, 36,36);
    }
  }
}
</script>




<style scoped>
.canvas-wrapper {
  display: grid;
  position: relative;
}
#canvas {
  background-color: #f9f9f9;
  z-index: 0;
}
#cursor {
  z-index: 1;
  pointer-events: none;
}
.active {
  background-color: #dea878 !important;
}
.tools {
  margin: 0;
  padding: 0;
}
.tools li{
  padding: 4px;
  background-color: #c8c8c8;
  border-left: 1px solid #abaaaa;
}
.tools li:not(:last-child) {
  border-bottom: 1px solid #abaaaa;
}
.draw-area canvas {
  position: absolute;
  left: 0;
  top: 0;
  border: 2px solid #c8c8c8;
  border-radius: 10px 0 10px 10px;
}
</style>