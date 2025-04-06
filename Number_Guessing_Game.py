import random

top_of_range = input("Enter a number: ")
try:
    top_of_range = int(top_of_range)
except ValueError:
    print("Please enter a number next time.")
    quit()
if top_of_range <= 0:
    print("Please enter a number greater than 0 next time.")
    quit()
r = random.randrange(11)
print("Welcome to the Number Guessing Game!")
playing = input("Do you want to play? (yes/no): ")
if playing.lower() != "yes":
    quit()
print("Great! Let's start the game.")
print("You will be asked to guess a number between 0 and", top_of_range)
print("You have 3 attempts to guess the number.")
print("Let's start the game.")
attempts = 0
while attempts < 3:
    guess = input("Enter your guess: ")
    try:
        guess = int(guess)
    except ValueError:
        print("Please enter a number next time.")
        quit()
    if guess < 0 or guess > top_of_range:
        print("Please enter a number between 0 and", top_of_range)
        continue
    if guess == r:
        print("Congratulations! You guessed the number!")
        break
    elif guess < r:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    attempts += 1
if attempts == 3:
    print("Sorry! You have used all your attempts.")
    print("The correct number was", r)
    1