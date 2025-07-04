"""Rock Paper Scissors game logic."""

import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
    """Return a random choice from rock, paper, or scissors."""
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    """Return the winner: 'user', 'computer', or 'tie'."""
    if player_choice == computer_choice:
        return "tie"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

def is_valid_choice(choice):
    """Check if the choice is valid."""
    return choice in choices

def play_game():
    """Run the Rock Paper Scissors game loop."""
    user_score = 0
    computer_score = 0

    while True:
        player_choice = input("Rock, Paper, or Scissors? (or 'exit' to quit): ").lower()
        if player_choice == "exit":
            break
        if not is_valid_choice(player_choice):
            print("Invalid choice.")
            continue

        computer = get_computer_choice()
        print(f"Computer chose: {computer}")
        result = determine_winner(player_choice, computer)

        if result == "tie":
            print("It's a tie.")
        elif result == "user":
            print("You win!")
            user_score += 1
        else:
            print("Computer wins!")
            computer_score += 1

    print(f"\nFinal Score — You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("🎉 You are the winner!")
    elif computer_score > user_score:
        print("🎉 Computer wins overall!")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    play_game()
