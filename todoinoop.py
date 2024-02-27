class Todo:
    def __init__(self):
        self.tasks = self.read_from_file()

    def read_from_file(self):
        with open('tasks.txt', 'r') as file:
            tasks = file.read().splitlines()
            return tasks

    def write_to_file(self, tasks):
        with open("tasks.txt", "w") as file:
            for task in tasks:
                file.write(f"{task}\n")
    
    def list_tasks(self):
        if len(self.tasks) > 0:
            print("\nTo-do List: ")
            for i, task in enumerate(self.tasks):
                print(f"{i + 1}. {task}")

    def run(self):
        while True:
            self.list_tasks()

            user_input = input("Enter 'add', 'mark', 'remove' or 'quit': ").lower()

            if user_input == "quit":
                print("Goodbye!")
                self.write_to_file(self.tasks)
                break
            
            elif user_input == "add":
                task = input("Enter a task: ")
                self.tasks.append(task)

            elif user_input == "mark":
                task_id = int(input("Enter the task id to mark as completed: ")) - 1

                if task_id < len(self.tasks) and task_id >= 0:
                    print("Task marked as completed: ", self.tasks[task_id])
                    self.tasks[task_id] = f"{self.tasks[task_id]} - COMPLETED"
                else:
                    print("Invalid task id")
            
            else:
                task_id = int(input("Enter the task id to remove: ")) - 1

                if task_id < len(self.tasks) and task_id >= 0:
                    print("Task removed: ", self.tasks[task_id])
                    del self.tasks[task_id]
                else:
                    print("Invalid task id")
        

todo = Todo()
todo.run()