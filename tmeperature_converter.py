# This program converts temperatures between Celsius and Fahrenheit.
# It's useful for beginners to understand basic math and conditionals in Python.

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32  # Formula to convert Celsius to Fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9  # Formula to convert Fahrenheit to Celsius

def main():
    print("Temperature Converter")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    try:
        choice = input("Enter choice: ")

        if choice == '1':
            c = float(input("Enter temperature in Celsius: "))
            print(f"{c}°C is equal to {celsius_to_fahrenheit(c):.2f}°F")
        elif choice == '2':
            f = float(input("Enter temperature in Fahrenheit: "))
            print(f"{f}°F is equal to {fahrenheit_to_celsius(f):.2f}°C")
        else:
            print("Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# This ensures the code runs only when the script is executed directly
if __name__ == "__main__":
    main()
