// todo.js

class TodoList {
    constructor() {
      this.tasks = [];
    }
    addTask(task) {
      this.tasks.push({ task, complete: false });
    }
    markTaskComplete(index) {
      if (index >= 0 && index < this.tasks.length) {
        this.tasks[index].complete = true;
      } else {
        console.log("Invalid task index");
      }
    }
    listAllTasks() {
      console.log("Tasks:");
      this.tasks.forEach((task, index) => {
        console.log(`${index + 1}. ${task.task} - ${task.complete ? 'Complete' : 'Incomplete'}`);
      });
    }
  }
  export default TodoList;
  