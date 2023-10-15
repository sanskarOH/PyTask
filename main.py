from task import *

# Main program loop
while True:
    print("\nTask Management System")
    print("1. Display Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Save Tasks to File")
    print("6. Load Tasks from File")
    print("7. Quit")
    choice = input("Enter your choice: ")

    if choice == '1':
        display_task()
    elif choice == '2':
        title = input("Enter the task title: ")
        description = input("Enter the task description: ")
        create_task(title, description)
    elif choice == '3':
        display_task()
        task_index = int(input("Enter the task index to mark as completed: "))
        change_status(task_index)
    elif choice == '4':
        display_task()
        task_index = int(input("Enter the task index to delete: "))
        delete_task(task_index-1)
    elif choice == '5':
         filename = input("Enter the filename to save tasks: ")
         save_tasks(filename)
    elif choice == '6':
         filename = input("Enter the filename to load tasks from: ")
         load_tasks(filename)
    elif choice == '7':
        break
    else:
        print("Invalid choice. Please try again.")
print(f"Thank you for using the Task Management System.")

   