#3 To-Do List

tasks = []

def menu():
    print("Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Exit")

def getchoice():
    while True:
        try:
            choice = int(input("Enter choice (1-4): "))
            if choice > 4 or choice < 1:
                print("Invalid choice\n")
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter a number.\n")

def operation(choice):
    if choice == 1:
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!\n")
    elif choice == 2:
        task = input("Enter task to remove: ")
        if task in tasks:
            tasks.remove(task)
            print("Task removed successfully!\n")
        else:
            print("Task not found!\n")
    elif choice == 3:
        print("Tasks:")
        for task in tasks:
            print(task, "\n")
    elif choice == 4:
        pass
    else:
        print("Invalid choice\n")

while True:
    menu()
    choice = getchoice()
    operation(choice)
    if choice == 4:
        break
