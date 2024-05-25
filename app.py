import random

# create a rock paper scissors game using python with GitHub Copilot

print("Welcome to Rock, Paper, Scissors!")
player_score = 0
computer_score = 0

def compute_selected_user_choice(player_score, computer_score, user_choice, computer_choice):
    if user_choice == computer_choice:
        print(f"Both players selected {user_choice}. It's a tie!")
    elif user_choice == "rock":
        if computer_choice == "scissors":
            print("Rock smashes scissors! You win!")
            player_score += 1
        else:
            print("Paper covers rock! You lose.")
            computer_score += 1
    elif user_choice == "paper":
        if computer_choice == "rock":
            print("Paper covers rock! You win!")
            player_score += 1
        else:
            print("Scissors cuts paper! You lose.")
            computer_score += 1
    elif user_choice == "scissors":
        if computer_choice == "paper":
            print("Scissors cuts paper! You win!")
            player_score += 1
        else:
            print("Rock smashes scissors! You lose.")
            computer_score += 1

while True:
    print("Enter your choice [rock, paper, scissors]: ")
    user_choice = input()
    user_choice = user_choice.lower()
    possible_choices = ["rock", "paper", "scissors"]
    if user_choice not in possible_choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue

    computer_choice = random.choice(possible_choices)
       
    print(f"\nYou chose {user_choice}, computer chose {computer_choice}.\n")

    compute_selected_user_choice(player_score, computer_score, user_choice, computer_choice)

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break

print(f"\nPlayer score: {player_score}")
print(f"Computer score: {computer_score}")
print("Goodbye!")
