#6 Compiled

def menu():
    print("\nMenu:")
    print("1. Simple Calculator")
    print("2. Temperature Converter")
    print("3. To-Do List")
    print("4. Number Guessing Game")
    print("5. Student Grade Calculator")
    print("6. Exit")


def getchoice():
    while True:
        try:
            choice = int(input("Enter choice (1-6): "))
            if choice > 6 or choice < 1:
                print("Invalid choice\n")
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def operation(choice):
    if choice == 1:
        def menu():
            print("\nMenu:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Exit")

        def getchoice():
            while True:
                try:
                    choice = int(input("Enter choice (1-5): "))
                    if choice > 5 or choice < 1:
                        print("Invalid choice\n")
                    else:
                        return choice
                except ValueError:
                    print("Invalid input. Please enter a number.\n")

        def getnum(msg):
            getnum = float(input(msg))
            return getnum

        def operation(choice):
            global num1
            global num2
            num1 = getnum("Enter first number: ")
            num2 = getnum("Enter second number: ")

            if choice == 1:
                result = num1 + num2
                print(f"Result: {result}\n")
            elif choice == 2:
                result = num1 - num2
                print(f"Result: {result}\n")
            elif choice == 3:
                result = num1 * num2
                print(f"Result: {result}\n")
            elif choice == 4:
                try:
                    result = num1 / num2
                    print(f"Result: {result}\n")
                except ZeroDivisionError:
                    print("Enter numbers other than zero\n")
            elif choice == 5:
                pass
            else:
                print("Invalid choice")

        while True:
            menu()
            choice = getchoice()
            if choice == 5:
                break
            operation(choice)
    elif choice == 2:
        def menu():
            print("\nMenu:")
            print("1. Convert Celsius to Fahrenheit")
            print("2. Convert Fahrenheit to Celsius")
            print("3. Exit")

        def getchoice():
            while True:
                try:
                    choice = int(input("Enter choice (1-3): "))
                    if choice > 3 or choice < 1:
                        print("Invalid choice\n")
                    else:
                        return choice
                except ValueError:
                    print("Invalid input. Please enter a number.\n")

        def main(choice):
            if choice == 1:
                celsius = float(input("Enter temperature in Celsius: "))
                result = (celsius * 9/5) + 32
                print(f"Temperature in Fahrenheit: {result}\n")
            elif choice == 2:
                fahrenheit = float(input("Enter temperature in Fahrenheit: "))
                result = (fahrenheit - 32) * 5/9
                print(f"Temperature in Celsius: {result}\n")
            elif choice == 3:
                pass
            else:
                print("Invalid choice\n")

        while True:
            menu()
            choice = getchoice()
            if choice == 3:
                break
            main(choice)
    elif choice == 3:
        tasks = []

        def menu():
            print("\nMenu:")
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
            if choice == 4:
                break
            operation(choice)
    elif choice == 4:
        import random

        def menu():
            print("\nMenu:")
            print("1. Play Number Guessing Game")
            print("2. Exit")
        
        def getchoice():
            while True:
                try:
                    choice = int(input("Enter choice (1-2): "))
                    if choice > 2 or choice < 1:
                        print("Invalid choice\n")
                    else:
                        return choice
                except ValueError:
                    print("Invalid input. Please enter a number.\n")
        
        def operation(choice):
            if choice == 1:
                number = random.randint(1, 100)
                attempts = 0
        
                while attempts < 3:
                    try:
                        guess = int(input("Enter your guess (1-100): "))
                        if guess < 1 or guess > 100:
                            print("Invalid guess. Please enter a number between 1 and 100.\n")
                            continue
                    except ValueError:
                        print("Invalid input. Please enter a number.\n")
                        continue
        
                    attempts += 1
        
                    if guess == number:
                        print(f"🎉 Congratulations! You guessed the number in {attempts} attempt/s\n")
                        return
                    elif guess < number:
                        print("Too low!\n")
                    else:
                        print("Too high!\n")
        
                print(f"The random number was: {number}\n")
        
        while True:
            menu()
            choice = getchoice()
            if choice == 2:
                break
            operation(choice)
    elif choice == 5:
        scores = []

        def menu():
            print("\nMenu:")
            print("1. Add Score")
            print("2. Calculate Average")
            print("3. Exit")
        
        def getchoice():
            while True:
                try:
                    choice = int(input("Enter choice (1-3): "))
                    if choice > 3 or choice < 1:
                        print("Invalid choice\n")
                    else:
                        return choice
                except ValueError:
                    print("Invalid input. Please enter a number.\n")
        
        def operation(choice):
            if choice == 1:
              try:
                score = float(input("Enter score: "))
                if score > 100 or score < 1:
                  print("Invalid choice\n")
                else:
                  scores.append(score)
                  print("Score added successfully!\n")
              except ValueError:
                    print("Invalid input. Please enter a number.\n")
            elif choice == 2:
                if len(scores) > 0:
                    average = sum(scores) / len(scores)
                    print(f"Average score: {average}\n")
                else:
                    print("No scores available to calculate average.\n")
            elif choice == 3:
                pass
            else:
                print("Invalid choice\n")
        
        while True:
            menu()
            choice = getchoice()
            if choice == 3:
                break
            operation(choice)
    elif choice == 6:
        pass

while True:
    menu()
    choice = getchoice()
    if choice == 6:
        break
    operation(choice)
