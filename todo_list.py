def show_tasks(tasks):
    """Display all tasks with their completion status."""
    if not tasks:
        print("\nYour to-do list is empty.")
        return

    print("\nYour To-Do List")
    print("-" * 30)

    for number, task in enumerate(tasks, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{number}. [{status}] {task['title']}")


def add_task(tasks):
    """Add a new task to the list."""
    title = input("Enter the task: ").strip()

    if title:
        tasks.append({
            "title": title,
            "completed": False
        })
        print("Task added.")
    else:
        print("Task title cannot be empty.")


def choose_task(tasks, prompt):
    """Ask the user to select a task by its number."""
    if not tasks:
        print("There are no tasks to choose from.")
        return None

    show_tasks(tasks)

    try:
        number = int(input(prompt))
        if 1 <= number <= len(tasks):
            return number - 1
        print("That task number is not on the list.")
    except ValueError:
        print("Please enter a valid whole number.")

    return None


def complete_task(tasks):
    """Mark a task as completed."""
    task_index = choose_task(tasks, "Enter the number of the task to complete: ")

    if task_index is not None:
        tasks[task_index]["completed"] = True
        print("Task marked as complete.")


def delete_task(tasks):
    """Delete a task from the list."""
    task_index = choose_task(tasks, "Enter the number of the task to delete: ")

    if task_index is not None:
        removed_task = tasks.pop(task_index)
        print(f"Deleted: {removed_task['title']}")


def main():
    tasks = []

    while True:
        print("\nTo-Do List App")
        print("1. View tasks")
        print("2. Add a task")
        print("3. Mark a task as complete")
        print("4. Delete a task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose an option from 1 to 5.")


if __name__ == "__main__":
    main()