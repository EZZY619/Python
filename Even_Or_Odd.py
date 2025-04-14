
"""
Even or Odd Checker

This simple program asks the user to enter a number and tells them
whether it is even or odd. It's a great beginner project to learn about
input, conditionals, and number operations in Python.
"""

def check_even_odd():
    try:
        # Ask the user to input a number
        number = int(input("Enter a number: "))

        # Check if the number is even or odd using the modulo operator
        if number % 2 == 0:
            print(f"{number} is even.")
        else:
            print(f"{number} is odd.")
    except ValueError:
        # Handle invalid input that is not an integer
        print("Please enter a valid integer.")

# This makes sure the function runs only if the script is run directly
if __name__ == "__main__":
    check_even_odd()
