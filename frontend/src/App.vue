<template>
  <div id="app">
    <h1>Todo app</h1>
    <Todo />
    <TodoEditor />
  </div>
</template>

<script>
import Todo from './components/Todo'
import TodoEditor from './components/TodoEditor'

export default {
  name: 'App',
  components: {
    Todo,
    TodoEditor
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
