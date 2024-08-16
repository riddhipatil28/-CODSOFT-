import random


def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"


def play_game():
    user_score = 0
    computer_score = 0
    
    while True:
        print("\n--- Rock, Paper, Scissors ---")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

       
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice, please try again.")
            continue

        
        computer_choice = get_computer_choice()

        
        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        
        winner = determine_winner(user_choice, computer_choice)
        
        if winner == "tie":
            print("It's a tie!")
        elif winner == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1
        
        
        print(f"Score - You: {user_score}, Computer: {computer_score}")
        
        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    
    print("\nFinal Score:")
    print(f"You: {user_score} | Computer: {computer_score}")
    print("Thanks for playing!")


play_game()
