tasks = []

def add_task():
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task '{task}' added successfully!")

def view_tasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Your to-do list:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def remove_task():
    view_tasks()
    try:
        task_number = int(input("Enter the task number to remove: "))
        if 1 <= task_number <= len(tasks):
            removed_task = tasks.pop(task_number - 1)
            print(f"Task '{removed_task}' removed successfully!")
        else:
            print("Invalid task number. Please try again.")
    except ValueError:
        print("Invalid input. Please enter a valid task number.")

def main():
    while True:
        print("\n--- To-Do List ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print("Goodbye! Have a productive day!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
