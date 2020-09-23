<template>
  <div class="hello">
    <div class="todo_container" v-for="todo in todos" :key="todo.name">
      <h2>{{ todo.name }}</h2>
      <p>{{ todo.description }}</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Todo',
  data: () => ({
    todos: [],
    editing: {
      name: '',
      description: ''
    }
  }),
  async created() {
    const r = await fetch('/api/v1/todos')

    if(r.status === 200) {
      const rawJson = await r.json()
      console.log(rawJson)
      this.todos = rawJson.payload
    }else{
      alert("Errored")
    }

  },
  props: {
    msg: String
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

