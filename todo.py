import os

# Function to clear the console screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to load tasks from file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            return [task.strip() for task in tasks]
    except FileNotFoundError:
        return []

# Function to save tasks to file
def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Function to display menu
def display_menu():
    clear_screen()
    print("To-Do List Application\n")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")

# Function to view tasks
def view_tasks(tasks):
    clear_screen()
    print("Tasks:")
    if tasks:
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks")

# Function to add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to mark task as completed
def mark_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to mark as completed: ")) - 1
    tasks.pop(task_index)
    print("Task marked as completed!")

# Function to remove task
def remove_task(tasks):
    view_tasks(tasks)
    task_index = int(input("Enter the task number to remove: ")) - 1
    tasks.pop(task_index)
    print("Task removed successfully!")

# Main function
def main():
    tasks = load_tasks()
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
