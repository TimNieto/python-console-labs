from input_utils import get_menu_choice, get_required_text


def display_menu():
    print("\nTo-Do List")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")


def add_task(tasks):
    task = get_required_text("Enter task: ")
    tasks.append(task)
    print("Task added successfully.\n")


def remove_task(tasks):
    if not tasks:
        print("No tasks available to remove.\n")
        return

    view_tasks(tasks)
    task_number = get_menu_choice("Enter task number to remove: ", 1, len(tasks))
    removed_task = tasks.pop(task_number - 1)
    print(f"Removed task: {removed_task}\n")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.\n")
        return

    print("\nTasks:")
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task}")
    print()


def run_todo_list():
    tasks = []

    while True:
        display_menu()
        choice = get_menu_choice("Enter choice (1-4): ", 1, 4)

        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            remove_task(tasks)
        elif choice == 3:
            view_tasks(tasks)
        elif choice == 4:
            print("Exiting to-do list.")
            break


if __name__ == "__main__":
    run_todo_list()