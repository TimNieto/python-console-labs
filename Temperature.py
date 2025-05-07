#2 Temperature Converter

def menu():
    print("Menu:")
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
        result = "Invalid choice\n"

while True:
    menu()
    choice = getchoice()
    main(choice)
    if choice == 3:
        break
