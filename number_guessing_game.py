"""
    A simple number guessing game.
    The user has 3 attempts to guess a randomly generated number between 1 and 10.
    Provides feedback after each guess.
"""
import random #This helps import random numbers

def guessing_game():  #Definition of the function

  
  # Generate a random number between 1 and 10
  secret_no =random.randint(1,10) 
  attempts =3

#Loops through all the attempts
  for attempt in range(1,attempts+1):

    try:
      guess = int(input(f"Attempt {attempt}/{attempts}: ")) #Gets the user's guess, then converts it into an integer

      if guess == secret_no:
        print("You guessed the correct number!")
        break #exits the loop if the guess is correct
      elif guess < secret_no:
        print("Too low! Try again") 
      else:
        print("Too high try again")
    except ValueError:
        print("Invalid number") #Throws an error when the input isn't an integer since we converted the guess into an integer
  else:
    print(f"You are out of attempts, the secret number is {secret_no}!") #Alerts the user when the user is out of attempts and reveals the secret number



if __name__ =="__main__":
  guessing_game()
