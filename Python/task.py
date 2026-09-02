def task_manager():
    print("===========Tasks Lists===========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")        
    input_choice = input("Enter your choice (1-5): ")
    Tasks = []
    if input_choice == "1":
        task = input("Enter the task: ")
        Tasks.append(task)
        print(f"Task '{task}' added successfully.")
        print("Current Tasks List:")
        for index, task in enumerate(Tasks, start=1):
            print(f"{index}. {task}")
    elif input_choice == "2":
        if not Tasks:
            print("No tasks available.")
        else:
            print("Tasks List:")
        for index, task in enumerate(Tasks, start=1):
            print(f"{index}. {task}")
    elif input_choice == "3":
        if not Tasks:
            print("No tasks available.")
        else:
            task_number = int(input("Enter the task number to mark as complete: "))
            if 1 <= task_number <= len(Tasks):
                completed_task = Tasks.pop(task_number - 1)
                print(f"Task '{completed_task}' marked as complete.")
            else:
                print("Invalid task number.")
    elif input_choice == "4":
        if not Tasks:
            print("No tasks available.")
        else:
            task_number = int(input("Enter the task number to delete: "))
            if 1 <= task_number <= len(Tasks):
                deleted_task = Tasks.pop(task_number - 1)
                print(f"Task '{deleted_task}' deleted successfully.")
            else:
                print("Invalid task number.")
    elif input_choice == "5":
        print("Exiting the task manager.")

while True:
    choice = input("Do you want to manage tasks? (yes/no): ")
    if choice.lower() == "yes":
        task_manager()
      
        
    if choice.lower() == "no":
        print("Exiting the task manager.")
        break
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")
