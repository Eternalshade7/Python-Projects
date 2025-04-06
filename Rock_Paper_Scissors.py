import random

user_wins = 0
computer_wins = 0
options = ["rock", "paper", "scissors"]
while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print(f"Computer picked {computer_pick}.")

    if user_input == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
        continue

    if user_input == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
        continue
    if user_input == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
        continue
    if user_input == computer_pick:
        print("It's a tie!")
        continue
    print("You lose!")
    computer_wins += 1
print(f"You won {user_wins} times.")
print(f"The computer won {computer_wins} times.")
print("Goodbye!")
# This is a simple Rock, Paper, Scissors game where the user can play against the computer.
# The user can input their choice, and the computer randomly selects its choice.
# The game keeps track of the number of wins for both the user and the computer.
# The game continues until the user decides to quit by entering 'Q'.
# The game is case-insensitive, so the user can enter their choice in any case.
# The game uses a while loop to keep running until the user quits.
# The game uses the random module to generate a random choice for the computer.
# The game uses a list to store the options for the game.
# The game uses if statements to determine the winner based on the user's and computer's choices.   