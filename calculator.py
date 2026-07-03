from input_utils import get_float, get_menu_choice


def display_menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")


def calculate(choice, first_number, second_number):
    if choice == 1:
        return first_number + second_number

    if choice == 2:
        return first_number - second_number

    if choice == 3:
        return first_number * second_number

    if choice == 4:
        if second_number == 0:
            print("Cannot divide by zero.\n")
            return None

        return first_number / second_number

    return None


def run_calculator():
    while True:
        display_menu()
        choice = get_menu_choice("Enter choice (1-5): ", 1, 5)

        if choice == 5:
            print("Exiting calculator.")
            break

        first_number = get_float("Enter first number: ")
        second_number = get_float("Enter second number: ")
        result = calculate(choice, first_number, second_number)

        if result is not None:
            print(f"Result: {result}\n")


if __name__ == "__main__":
    run_calculator()