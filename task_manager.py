def tasks():
    tasks = []
    print("Welcome to Task Manager:")

    try:
        num_tasks = int(input("Enter how many tasks you want to add: "))
    except ValueError:
        print("Invalid input! Please enter an integer.")
        return  # Exit the function if the input is invalid

    # Add tasks based on user input
    for i in range(1, num_tasks + 1):
        task_name = input(f"Enter task {i}: ")
        tasks.append(task_name)

    # Display the current list of tasks
    print(f"Your tasks are:\n{tasks}")

    while True:
        operation = input("Enter 1 - Add\n2 - Update\n3 - View\n4 - Delete\n5 - Exit\n")

        if operation == '1':  # Add a task
            add = input("Enter the new task: ")
            tasks.append(add)
            print(f"Task added successfully: {tasks}")

        elif operation == '2':  # Update a task
            updated_val = input("Enter the task you want to update: ")
            task_found = False
            for index, task in enumerate(tasks):
                if updated_val.lower() == task.lower():  # case-insensitive check
                    task_found = True
                    up = input("Enter the new task: ")
                    tasks[index] = up
                    print(f"Task updated successfully: {tasks}")
                    break
            if not task_found:
                print("Task not found.")

        elif operation == '3':  # View tasks
            if tasks:
                print("Your tasks are:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task}")
            else:
                print("No tasks to display.")

        elif operation == '4':  # Delete a task
            del_val = input("Enter the task you want to delete: ")
            task_found = False
            for task in tasks:
                if del_val.lower() == task.lower():  # case-insensitive check
                    task_found = True
                    tasks.remove(task)
                    print(f"Task deleted successfully: {tasks}")
                    break
            if not task_found:
                print("Task not found.")

        elif operation == '5':  # Exit
            print("Exiting Task Manager...")
            break

        else:  # Invalid input handling
            print("Invalid input, please choose a valid operation.")

# To run the function
tasks()
