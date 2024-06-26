# Function to load tasks from a file
def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

# Function to save tasks to a file
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

# Load tasks from file on program start
tasks = load_tasks()

def add_task(task):
    tasks.append(task)
    save_tasks()
    print(f"Task '{task}' added.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        save_tasks()
        print(f"Task '{task}' removed.")
    else:
        print(f"Task '{task}' not found in the list.")

def show_tasks():
    if tasks:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
    else:
        print("No tasks in the list.")

while True:
    print("\nChoose an option:")
    print("1. Add a task")
    print("2. Remove a task")
    print("3. Show all tasks")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        task = input("Enter task to add: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        show_tasks()
    elif choice == '4':
        print("Saving tasks and exiting program.")
        save_tasks()
        break
    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
