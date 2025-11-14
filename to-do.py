FILENAME = "tasks.txt"

def load_tasks():
    tasks = []
    try:
        with open(FILENAME, "r") as file:
            for line in file:
                tasks.append(line.strip())
    except FileNotFoundError:
        pass  # File will be created when saved
    return tasks

def save_tasks(tasks):
    with open(FILENAME, "w") as file:
        for task in tasks:
            file.write(task + "\n")


def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks found!")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")


def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added!")


def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            num = int(input("\nEnter task number to remove: "))
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}")
        except (ValueError, IndexError):
            print("Invalid task number!")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Save & Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            remove_task(tasks)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option. Try again.")


if __name__ == "__main__":
    main()