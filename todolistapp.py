# This is a simple command-line to-do list application.

def display_menu():
    """Displays the main menu options to the user."""
    print("\n--- To-Do List Menu ---")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Remove Task")
    print("5. Exit")
    print("-----------------------")

def view_tasks(tasks):
    """Displays all tasks in the to-do list."""
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\n--- Your To-Do List ---")
        for i, task in enumerate(tasks):
            status = "✓" if task["completed"] else " "
            print(f"{i + 1}. [{status}] {task['name']}")
        print("-----------------------")

def add_task(tasks, task_name):
    """Adds a new task to the to-do list."""
    tasks.append({"name": task_name, "completed": False})
    print(f"Task '{task_name}' added successfully!")

def mark_task_complete(tasks, task_index):
    """Marks a task as complete based on its index."""
    if 0 <= task_index < len(tasks):
        tasks[task_index]["completed"] = True
        print(f"Task '{tasks[task_index]['name']}' marked as complete!")
    else:
        print("Invalid task number. Please try again.")

def remove_task(tasks, task_index):
    """Removes a task from the to-do list based on its index."""
    if 0 <= task_index < len(tasks):
        removed_task = tasks.pop(task_index)
        print(f"Task '{removed_task['name']}' removed successfully!")
    else:
        print("Invalid task number. Please try again.")

def main():
    """Main function to run the to-do list application."""
    tasks = []  # List to store tasks. Each task is a dictionary.

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            task_name = input("Enter the task to add: ")
            if task_name:
                add_task(tasks, task_name)
            else:
                print("Task name cannot be empty.")
        elif choice == '3':
            view_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the number of the task to mark as complete: "))
                    mark_task_complete(tasks, task_num - 1)  # Adjust for 0-based indexing
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '4':
            view_tasks(tasks)
            if tasks:
                try:
                    task_num = int(input("Enter the number of the task to remove: "))
                    remove_task(tasks, task_num - 1)  # Adjust for 0-based indexing
                except ValueError:
                    print("Invalid input. Please enter a number.")
        elif choice == '5':
            print("Exiting to-do list application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
