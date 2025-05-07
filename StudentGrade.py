#5 Student Grade Calculator

scores = []

def menu():
    print("Menu:")
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
    operation(choice)
    if choice == 3:
        break
