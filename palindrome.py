def is_palindrome(text: str) -> bool: # This function checks if the given string is a palindrome and returns a boolean value.
    """
    What the function(is_palindrome) does:
    Checks if a given string is a palindrome.
    Ignores spaces and is case-insensitive.

    Parameters:
    text (str): The string to check.

Returns:
    bool: True if the string is a palindrome, False otherwise.
    
    A palindrome is a word, phrase, or sequence of characters that reads the same forward and backward (ignoring spaces, punctuation, and sometimes capitalization). For example, madam, civic, etc
    """
    cleaned = text.lower().replace(" ", "") #converts the text to lowercases and makes it case-insensitive
    return cleaned == cleaned[::-1]  #checks if the parameter's value is a palindrome or not, then returns a boolean
"""
The block of code below is excellent for code reuseability because it controls the interaction between those who import the code and those who run it locally, 
It is helpful because it improves code flexibility once imported into another program or used in a different context. 
In other words, it is mainly used for code reusability but can also be used to debug or test the functionality of your code.
"""
if __name__ == "__main__":
    word = input("Enter a word or phrase to check: ") #requests for user input
    if is_palindrome(word):  #the process to check if it's a palindrome or not by using the function (is_palindrome)
        print("It's a palindrome!") #output, if true
    else:
        print("Not a palindrome.") #output, if false
