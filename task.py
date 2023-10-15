import os
import pickle
class Task:
    def __init__(self, title, description, status="Not Completed"):
        self.title = title
        self.description = description
        self.status = status
tasks = []

    # Function to add a new task with input validation for an empty title
def create_task(title, description, status="Not Completed"):
    if title.strip() == "":
        print("Task title cannot be empty. Please enter a valid title.")
    else:
        if status.strip() == "":
            status = "Not Completed"  # Fix the typo here

        task = Task(title, description, status)
        tasks.append(task)
        print(f"Task '{title}' added.")

def display_task():
    if not tasks:
        print("No tasks to display.")
    else:
        print("Task List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. Title: {task.title}")
            print(f"   Description: {task.description}")
            print(f"   Status: {task.status}\n")
# def change_status(task_index):
#     if 1<= task_index <=len(tasks):
#         tasks[task_index].status = "Completed"
#     else:
#         print(f"Not a valid task index!!")
def change_status(task_index):
    if 1 <= task_index <= len(tasks):
        tasks[task_index - 1].status = "Completed"
        print(f"Task {task_index} marked as completed.")
    else:
        print("Invalid task index. Please try again.")         

def delete_task(task_index):
    if 1<= task_index <= len(tasks):
        deleted_task = tasks.pop(task_index)
        print(f"Task '{deleted_task.title}' has been deleted.")
    else:
        print(f"Not a valid {task_index} task index!!")   

# Function to save tasks to a file
def save_tasks(filename):
    with open(filename, 'wb') as file:
        pickle.dump(tasks, file)
    print(f"Tasks saved to '{filename}'.")

# Function to load tasks from a file
def load_tasks(filename):
    if os.path.exists(filename):
        with open(filename, 'rb') as file:
            loaded_tasks = pickle.load(file)
        tasks.extend(loaded_tasks)
        print(f"Tasks loaded from '{filename}'.")
    else:
        print(f"'{filename}' does not exist. No tasks loaded.")



 