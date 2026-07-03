from input_utils import get_float, get_menu_choice


def display_menu():
    print("\nTemperature Converter")
    print("1. Convert Celsius to Fahrenheit")
    print("2. Convert Fahrenheit to Celsius")
    print("3. Exit")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


def run_temperature_converter():
    while True:
        display_menu()
        choice = get_menu_choice("Enter choice (1-3): ", 1, 3)

        if choice == 3:
            print("Exiting temperature converter.")
            break

        if choice == 1:
            celsius = get_float("Enter temperature in Celsius: ")
            result = celsius_to_fahrenheit(celsius)
            print(f"Temperature in Fahrenheit: {result:.2f}\n")

        elif choice == 2:
            fahrenheit = get_float("Enter temperature in Fahrenheit: ")
            result = fahrenheit_to_celsius(fahrenheit)
            print(f"Temperature in Celsius: {result:.2f}\n")


if __name__ == "__main__":
    run_temperature_converter()
