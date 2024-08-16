# To-Do List Application

tasks = []

while True:
    print("\n--- To-Do List Application ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5): ")
    
    
    if choice == '1':
        task_description = input("Enter task description: ")
        tasks.append(task_description)
        print("Task added successfully!")
    
    
    elif choice == '2':
        if tasks:
            print("\nYour To-Do List:")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks to display.")
    

    elif choice == '3':
        if tasks:
            task_number = int(input("Enter the number of the task to update: "))
            if 1 <= task_number <= len(tasks):
                new_description = input("Enter new task description: ")
                tasks[task_number - 1] = new_description
                print("Task updated successfully!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to update.")
    
  
    elif choice == '4':
        if tasks:
            task_number = int(input("Enter the number of the task to delete: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' deleted successfully!")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to delete.")
    
    
    elif choice == '5':
        print("Exiting the To-Do List Application.")
        break
    
    
    else:
        print("Invalid choice, please try again.")
