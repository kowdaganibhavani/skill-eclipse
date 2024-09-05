import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks, title, priority, due_date):
    task = {
        'title': title,
        'priority': priority,
        'due_date': due_date,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task '{title}' added successfully!")

def remove_task(tasks, task_index):
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        save_tasks(tasks)
        print(f"Task '{removed_task['title']}' removed successfully!")
    else:
        print("Invalid task number!")

def mark_task_completed(tasks, task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print(f"Task '{tasks[task_index]['title']}' marked as completed!")
    else:
        print("Invalid task number!")

def list_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks):
            status = "RIGHT" if task['completed'] else "X"
            print(f"{i + 1}. [{status}] {task['title']} (Priority: {task['priority']}, Due: {task['due_date']})")

def main():
    tasks = load_tasks()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Mark Task as Completed")
        print("4. List Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high/medium/low): ").lower()
            due_date = input("Enter due date (YYYY-MM-DD): ")
            add_task(tasks, title, priority, due_date)
        elif choice == '2':
            list_tasks(tasks)
            task_index = int(input("Enter task number to remove: ")) - 1
            remove_task(tasks, task_index)
        elif choice == '3':
            list_tasks(tasks)
            task_index = int(input("Enter task number to mark as completed: ")) - 1
            mark_task_completed(tasks, task_index)
        elif choice == '4':
            list_tasks(tasks)
        elif choice == '5':
            print("Exiting application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
