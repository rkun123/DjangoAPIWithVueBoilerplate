<template>
  <div class="todoEditor">
    <div class="section">
      <div class="label">NAME</div>
      <input type="text" v-model="todo.name">
    </div>
    <div class="section">
      <div class="label">DESCRIPTION</div>
      <textarea v-model="todo.description"></textarea><br />
      <button class="submit" v-on:click="post">追加</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'TodoEditor',
  data: () => ({
    todo: {
      name: '',
      description: ''
    }
  }),
  methods: {
    async post() {
      console.log(JSON.stringify(this.todo))
       await fetch('/api/v1/todos', {
         method: "POST",
         body: JSON.stringify(this.todo)
       })
       this.$emit('updated')
       this.todo.name = ''
       this.todo.description = ''
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.todoEditor {
  background-color: silver;
  width: 100%;
}
.section {
  padding: 1rem 0;
  margin: 1rem 0;
}
.section .label {
  margin-bottom: 1rem;
}
.section input[type="text"] {
  width: 80%;
  font-size: 1.5rem;
  padding: 0.2rem;
  border: none;
}
.section textarea {
  width: 80%;
  padding: 0.2rem;
  height: 5rem;
  border: none;
}
.section .submit {
  height: 2rem;
  padding: 0 2rem;
  border-radius: none;
  border: none;
  margin: 2rem 0;
}
.label {
  font-size: 1.2rem;
}
</style>

