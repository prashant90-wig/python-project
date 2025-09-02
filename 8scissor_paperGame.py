import random

def menu():
    print("\n====Scissor Paper Rock Game Menu====")
    print("1. Play the game vs computer.")
    print("2. See your score.")
    print("3. Exit game.")
    print("-" *30)

def get_choices():
    player_choice = input("\n**********Enter a choice between (Scissor/Paper/Rock)************").lower()
    option = ["scissor", "rock", "paper"]
    computer_choice = random.choice(option)
    while player_choice not in option:
        print("Invalid!!! Enter correct option :")
        player_choice = input("\nEnter a choice between (Scissor/Paper/Rock)").lower()
    choices = {"player" : player_choice, "computer" : computer_choice}
    return choices


def check_win(player, computer):
    global player_wins, computer_wins
    
    print(f"\nYou chose {player}")
    print(f"Computer chose {computer}")
    
    if player == computer:
        return "\nIt's a tie!\n"
    elif player == "rock":
        if computer == "scissor":
            player_wins += 1
            return "\n*****************Rock smashes scissors! You win!*****************\n"
        else:
            computer_wins += 1
            return "\n*****************Paper covers rock! You lose.*****************\n"
    elif player == "paper":
        if computer == "scissor":
            computer_wins += 1
            return "\n*****************Scissors tear paper, You lose.*****************\n"
        else:
            player_wins += 1
            return "\n*****************Paper covers rock! You Win!*****************\n"
    elif player == "scissor":
        if computer == "rock":
            computer_wins += 1
            return "\n*****************Rock smashes scissors! You lose.*****************\n"
        else:
            player_wins += 1
            return " \n*****************Scissors tear paper, You Win!*****************\n\n"

def show_score():
    print("===Your score ===")
    print(f"You: {player_wins} wins")
    print(f"Computer: {computer_wins} wins")
    print(f"Total games played: {player_wins + computer_wins}\n")

player_wins = 0
computer_wins = 0
while True:
    menu()

    choice = input("Enter your choice (1, 2 or 3): ")
    
    if choice == '1':
            choices = get_choices()
            result = check_win(choices["player"], choices["computer"])
            print(result)

    elif choice == '2':
        show_score()
    elif choice == '3':
        print("Exiting the game. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter 1, 2 or 3.")


