# This program checks the strength of a password based on its length and content
# It gives feedback to the user on how to improve their password

import string  # Imports character sets like letters, digits, and punctuation

def check_password_strength(password):
    # Minimum password length for strength check
    min_length = 8

    # Conditions to test
    has_upper = any(char.isupper() for char in password)  # Checks for uppercase letters
    has_lower = any(char.islower() for char in password)  # Checks for lowercase letters
    has_digit = any(char.isdigit() for char in password)  # Checks for digits
    has_special = any(char in string.punctuation for char in password)  # Checks for special characters

    # Evaluate strength
    if len(password) < min_length:
        return "Weak – Password is too short. Use at least 8 characters."
    elif not (has_upper and has_lower and has_digit and has_special):
        return "Moderate – Add uppercase, lowercase, numbers, and special characters for a stronger password."
    else:
        return "Strong – Good job! Your password is strong."

if __name__ == "__main__":
    user_password = input("Enter your password: ")
    result = check_password_strength(user_password)
    print("Password Strength:", result)
