from datetime import datetime  #Importation of the package, which will be useful in knowing the date that we are in, at the moment

def calculate_age(birth_year: int) -> int:  #function to calculate the age and denotes it to an interger, ensuring the output will be the same
    """
    Calculates the user's age based on the current year.

    Parameters:
        birth_year (int): The year the user was born.

    Returns:
        int: The user's age.
    """
    current_year = datetime.now().year   #getting the year we are currently in using the 'datetime' package
    return current_year - birth_year

if __name__ == "__main__":  
# This ensures the code below runs only when the script is executed locally. 
# If the script is imported as a module, the code below won't run. 
    print("Welcome to the Age Calculator!")

    try:   #The exceptional error handling ensures the user inputs the needed age format else it will throw and error (Please enter a valid year (e.g, 2000))
        birth_year = int(input("Enter your birth year (e.g, 2000): ").strip()) #Collecting the user's birthyear and stripping it off of any whitespaces
        age = calculate_age(birth_year)    #THe age is calculated and stored in the 'age' variable

        print(f"You are {age} years old in {datetime.now().year}.")
    except ValueError:
        print("Please enter a valid year (e.g, 2000).")
