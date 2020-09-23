<template>
  <div id="app">
    <h1>Todo app</h1>
    <Todo />
  </div>
</template>

<script>
import Todo from './components/Todo'

export default {
  name: 'App',
  components: {
    Todo,
  }
}
</script>

<style lang='scss'>
$mobile_width_threshold: 680px;
@media screen and (max-width: $mobile_width_threshold) {
  #app {
    width: 100%;
  }
}
@media screen and (min-width: $mobile_width_threshold) {
  #app {
    width: $mobile_width_threshold;
  }
}
body {
  text-align: center;
  margin: 0;
  background-color: #ddd;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  display: inline-block;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  padding: 0;
}
</style>
