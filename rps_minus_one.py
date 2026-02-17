import random #Importing the random module to handle random choices for the computer

#This function determines the outcome of the game: win, lose, or tie
def winner(user_choice, computer_choice):
    
    #Check if both choices are the same (tie)
    if user_choice == computer_choice:
        return "It's tie"
    # Check all winning combinations for the user
    elif (user_choice == 'rock' and computer_choice == 'scissors') or (user_choice == 'scissors' and computer_choice == 'paper') or (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    # Any other case means the user loses
    else:
        return "You lose!"

# This function runs the main game loop
def play_game():
    # List of valid choices
    choices =['rock', 'paper', 'scissors']
    print("Welcome to Rock-Paper-Scissors minus one!")

    while True:
        # Prompt the user to select two choices
        print("\nAvailable choices: rock, paper, and scissors")
        user_choice_1 = input("Enter your first choice: ").lower()
        user_choice_2 = input("Enter your second choice: ").lower()
         
        # Validate the user's choices
        if user_choice_1 not in choices or user_choice_2 not in choices:
            print("Invalid choices! Please select from available choices.")
            continue # Restart the loop if invalid input is given

        # Computer randomly selects two choices
        computer_choice_1 = random.choice(choices)
        computer_choice_2 = random.choice(choices)

        # Display the initial choices of both the user and the computer
        print(f"\nYou choose: {user_choice_1} and {user_choice_2}")
        print(f"Computer choose: {computer_choice_1} and {computer_choice_2}")

        # Prompt the user to remove one of their choices
        user_remove = input(f"\nChoose one to remove: ({user_choice_1} or {user_choice_2}) ").lower()
        if user_remove == user_choice_1:
            user_final = user_choice_2 # Keep the second choice
        elif user_remove == user_choice_2:
            user_final = user_choice_1 # Keep the first choice
        else:
            print("Invalid removal! Restarting the round.")
            continue # Restart the loop if invalid input is given

        # Computer randomly removes one of its choices
        computer_final = random.choice([computer_choice_1, computer_choice_2])
        
        # Determine the winner and display the result
        result = winner(user_final, computer_final)
        print(f"Your choice: {user_final} \nComputer choice: {computer_final}\n")
        print(result)

        # Ask the user if they want to play another round
        play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()
        if play_again == 'no':
            print("Thanks for playing!")
            break # Exit the loop to end the game
        elif play_again != "yes":
            print("Invalid input. Exiting the game....")
            break # Exit the loop if the input is invalid

# Entry point: Run the game only if the script is executed directly
if __name__ == "__main__":
    play_game()