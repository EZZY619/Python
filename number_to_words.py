# This program converts numbers into words using the num2words library
# In case you don't have the package, you can install it by using the command 'pip install num2word'

from num2words import num2words  # Import the num2words library

def number_to_words():
    try:
        # Get a number input from the user
        number = int(input("Enter a number to convert to words: "))
        
        # Convert the number to words
        words = num2words(number)
        
        # Display the result
        print(f"The number {number} in words is: {words}")
        
    except ValueError:
        # Handles non-integer inputs
        print("Please enter a valid integer!")

if __name__ == "__main__":
    number_to_words()
