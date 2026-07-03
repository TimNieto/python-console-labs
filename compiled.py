from calculator import run_calculator
from input_utils import get_menu_choice
from number_guess import run_number_guessing_game
from student_grade import run_student_grade_calculator
from temperature import run_temperature_converter
from todo import run_todo_list


def display_menu():
    print("\nPython Console Labs")
    print("1. Simple Calculator")
    print("2. Temperature Converter")
    print("3. To-Do List")
    print("4. Number Guessing Game")
    print("5. Student Grade Calculator")
    print("6. Exit")


def run_program(choice):
    if choice == 1:
        run_calculator()
    elif choice == 2:
        run_temperature_converter()
    elif choice == 3:
        run_todo_list()
    elif choice == 4:
        run_number_guessing_game()
    elif choice == 5:
        run_student_grade_calculator()


def main():
    while True:
        display_menu()
        choice = get_menu_choice("Enter choice (1-6): ", 1, 6)

        if choice == 6:
            print("Exiting Python Console Labs.")
            break

        run_program(choice)


if __name__ == "__main__":
    main()