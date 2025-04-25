import random  # Import the random module to allow the computer to randomly select a choice

# Print a welcome message for the player
print("Welcome to Rock, Paper, Scissors!")

# Define the valid choices the player and the computer can make
options = ["rock", "paper", "scissors"]

# Function to get the player's choice
def get_user_choice():
    # Prompt the user to enter their choice, converting it to lowercase to handle case insensitivity
    choice = input("Choose rock, paper, or scissors: ").lower()
    
    # Ensure the user enters a valid choice (rock, paper, or scissors)
    while choice not in options:
        print("That’s not a valid choice. Try again.")  # Inform the user of an invalid choice
        # Prompt again until the user enters a valid option
        choice = input("Choose rock, paper, or scissors: ").lower()
    
    return choice  # Return the user's choice

# Function to randomly generate the computer's choice
def get_computer_choice():
    return random.choice(options)  # Return a random choice from the options list

# Function to check who won the game based on user and computer choices
def check_winner(user, computer):
    # If both player and computer make the same choice, it's a tie
    if user == computer:
        return "It's a tie!"
    # Check if the user wins based on the rules of the game
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    # If none of the above, then the computer wins
    else:
        return "Computer wins!"

# Main game loop to allow the player to keep playing until they decide to stop
while True:
    # Get the user's choice
    user_choice = get_user_choice()
    # Get the computer's choice
    computer_choice = get_computer_choice()

    # Display both the user's and the computer's choices
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    
    # Check who won and display the result
    print(check_winner(user_choice, computer_choice))

    # Ask the user if they want to play again
    play_again = input("\nWanna play again? (yes/no): ").lower()
    
    # If the user types anything other than "yes", exit the game
    if play_again != "yes":
        print("Thanks for playing!")  # Display a thank-you message when the user ends the game
        break  # Exit the game loop
