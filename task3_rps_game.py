import random

choices = ("rock", "paper", "scissors") 
player_wins = 0
computer_wins = 0
draws = 0

while True:
    player_choice = input("rock, paper, scissors or q to quit: ").strip().lower()
    if player_choice == "q":
        break
    if player_choice not in choices:
        print("Invalid choice")
        continue
    computer_choice = random.choice(choices) #random.choice chooses a random element within the list, hence why i made a list in the first place
    print(f"Computer: {computer_choice}")
    if player_choice == computer_choice:
        print("It's a draw!")
        draws += 1
    elif (
        (player_choice == "rock" and computer_choice == "scissors")
        or (player_choice == "paper" and computer_choice == "rock")
        or (player_choice == "scissors" and computer_choice == "paper") # shorter way to write all the repeating if statements
    ):
        print("You win!")
        player_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1
        
print (f"You won {player_wins}, the computer won {computer_wins}, draws: {draws}")
