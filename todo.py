def write_to_file(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(f"{task}\n")

def read_from_file():
    with open('tasks.txt', 'r') as file:
        tasks = file.read().splitlines()
        return tasks
        

def todo_list():
    tasks = read_from_file()

    while True:
        # display list
        if len(tasks) > 0:
            print("\nTo-do List: ")
            for i, task in enumerate(tasks):
                print(f"{i + 1}. {task}")
        
        user_input = input("Enter 'add', 'mark', 'remove' or 'quit': ").lower()

        if user_input == "quit":
            print("Goodbye!")
            write_to_file(tasks)
            break
        
        elif user_input == "add":
            task = input("Enter a task: ")
            tasks.append(task)

        elif user_input == "mark":
            task_id = int(input("Enter the task id to mark as completed: ")) - 1

            if task_id < len(tasks) and task_id >= 0:
                print("Task marked as completed: ", tasks[task_id])
                tasks[task_id] = f"{tasks[task_id]} - COMPLETED"
            else:
                print("Invalid task id")
        
        else:
            task_id = int(input("Enter the task id to remove: ")) - 1

            if task_id < len(tasks) and task_id >= 0:
                print("Task removed: ", tasks[task_id])
                del tasks[task_id]
            else:
                print("Invalid task id")


todo_list()
