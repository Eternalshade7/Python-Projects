import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
name = input("What is your name? ")
print(f"Hello {name}, welcome to the Choose Your Own Adventure game!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way do you want to go? (left/right) ").lower()

if answer == "left":
    answer = input("You come to a river, you can walk around it or swim across. (walk/swim) ").lower()
    if answer == "swim":
        print("You swam across and were eaten by an alligator.")
    elif answer == "walk":
        print("You walked for many miles and found a treasure chest!")
    else:
        print("Not a valid option. You lose!")
elif answer == "right":
    answer = input("You come to a hill, you can climb it or go around it. (climb/go) ").lower()
    if answer == "climb":
        print("You climbed the hill and found a beautiful view!")
    elif answer == "go":
        print("You went around the hill and got lost in the woods.")
    else:
        print("Not a valid option. You lose!")
else:
    print("Not a valid option. You lose!")
# This is a simple text-based adventure game where the player makes choices to navigate through a story.        