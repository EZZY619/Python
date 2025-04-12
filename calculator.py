# This is a simple calculator program that can perform addition, subtraction,
# multiplication, and division. It's great for beginners learning Python basics.

def add(x, y):
    return x + y  # Adds two numbers

def subtract(x, y):
    return x - y  # Subtracts y from x

def multiply(x, y):
    return x * y  # Multiplies two numbers

def divide(x, y):
    if y != 0:
        return x / y  # Divides x by y, if y is not zero
    else:
        return "Error! Division by zero."  # Handles division by zero

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = input("Enter choice: ")
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            print("Result:", divide(num1, num2))
        else:
            print("Invalid input")  # When input is not 1-4
    except ValueError:
        print("Invalid input. Please enter numbers only.")  # Handles non-numeric input

# This ensures the code runs only when executed directly, not when imported
if __name__ == "__main__":
    main()
