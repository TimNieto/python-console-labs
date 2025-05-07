#1 Simple Calculator

def menu():
    print("Menu:")
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
    operation(choice)
    if choice == 5:
        break
