from input_utils import get_float, get_menu_choice


def display_menu():
    print("\nStudent Grade Calculator")
    print("1. Add Score")
    print("2. Calculate Average")
    print("3. Exit")


def add_score(scores):
    score = get_float("Enter score (0-100): ", 0, 100)
    scores.append(score)
    print("Score added successfully.\n")


def show_average(scores):
    if not scores:
        print("No scores available to calculate average.\n")
        return

    average = sum(scores) / len(scores)
    print(f"Average score: {average:.2f}\n")


def run_student_grade_calculator():
    scores = []

    while True:
        display_menu()
        choice = get_menu_choice("Enter choice (1-3): ", 1, 3)

        if choice == 1:
            add_score(scores)
        elif choice == 2:
            show_average(scores)
        elif choice == 3:
            print("Exiting student grade calculator.")
            break


if __name__ == "__main__":
    run_student_grade_calculator()