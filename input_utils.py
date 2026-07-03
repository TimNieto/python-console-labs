def get_menu_choice(prompt, minimum, maximum):
    while True:
        try:
            choice = int(input(prompt))

            if minimum <= choice <= maximum:
                return choice

            print(f"Invalid choice. Enter a number from {minimum} to {maximum}.\n")
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def get_float(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = float(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Invalid input. Enter a number greater than or equal to {minimum}.\n")
                continue

            if maximum is not None and value > maximum:
                print(f"Invalid input. Enter a number less than or equal to {maximum}.\n")
                continue

            return value
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def get_int(prompt, minimum=None, maximum=None):
    while True:
        try:
            value = int(input(prompt))

            if minimum is not None and value < minimum:
                print(f"Invalid input. Enter a number greater than or equal to {minimum}.\n")
                continue

            if maximum is not None and value > maximum:
                print(f"Invalid input. Enter a number less than or equal to {maximum}.\n")
                continue

            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.\n")


def get_required_text(prompt):
    while True:
        value = input(prompt).strip()

        if value:
            return value

        print("Input cannot be empty.\n")