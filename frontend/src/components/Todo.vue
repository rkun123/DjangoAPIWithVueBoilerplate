<template>
  <div class="todo">
    <div class="todo_container" v-for="todo in todos" :key="todo.id">
      <h2>{{ todo.name }}</h2>
      <p>{{ todo.description }}</p>
      <button v-on:click="deleteTodos(todo.id)">Delete</button>
    </div>
    <hr />
    <TodoEditor @updated="update" />
  </div>
</template>

<script>
import TodoEditor from './TodoEditor'
export default {
  components: {
    TodoEditor
  },
  name: 'Todo',
  data: () => ({
    todos: [],
    editing: {
      name: '',
      description: ''
    }
  }),
  async created() {
    this.update()
  },
  props: {
    msg: String
  },
  methods: {
    async update() {
      const r = await fetch('/api/v1/todos')

      if(r.status === 200) {
        const rawJson = await r.json()
        console.log(rawJson)
        this.todos = rawJson.payload
      }else{
        alert("Errored")
      }
    },
    async deleteTodos(id) {
      const r = await fetch(`/api/v1/todos/${id}`, {
        method: 'DELETE'
      })
      if(r.status === 200) {
        const idx = this.todos.findIndex((todo) => (todo.id === id))
        this.todos.splice(idx, idx)
      }
      this.update()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.todo {
  width: 100%;
}
.todo_container {
  /*border: solid 2px black;*/
  background-color: silver;
  margin: 1rem 0;
  padding: 1rem;
}
.todo_container h2 {
  display: inline-block;
  padding: 0 3rem;
  border-bottom: solid 1px black;
}
</style>

