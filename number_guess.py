import random

from input_utils import get_int, get_menu_choice


def display_menu():
    print("\nNumber Guessing Game")
    print("1. Play")
    print("2. Exit")


def play_game():
    secret_number = random.randint(1, 100)
    max_attempts = 3

    print("\nGuess the number from 1 to 100.")
    print(f"You have {max_attempts} attempts.\n")

    for attempt in range(1, max_attempts + 1):
        guess = get_int("Enter your guess (1-100): ", 1, 100)

        if guess == secret_number:
            print(f"Congratulations! You guessed the number in {attempt} attempt(s).\n")
            return

        if guess < secret_number:
            print("Too low.\n")
        else:
            print("Too high.\n")

    print(f"The correct number was: {secret_number}\n")


def run_number_guessing_game():
    while True:
        display_menu()
        choice = get_menu_choice("Enter choice (1-2): ", 1, 2)

        if choice == 1:
            play_game()
        elif choice == 2:
            print("Exiting number guessing game.")
            break


if __name__ == "__main__":
    run_number_guessing_game()