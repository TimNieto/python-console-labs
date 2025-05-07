#4 Number Guessing Game

import random

def menu():
    print("Menu:")
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
    operation(choice)
    if choice == 2:
        break
