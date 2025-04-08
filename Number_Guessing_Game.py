# 🎮 Number Guessing Game by Naksh (aka Shade)
# Upload-ready with instructions and clean code!
# 🔁 The game lets users guess a number within a chosen range.
# They get 5 tries and can play again after each round.

import random

def play_game():
    tries = 0  # Count number of attempts

    print("\n🎯 Welcome to the Number Guessing Game!")

    # Ask user to set the maximum range value
    x = int(input("Enter the maximum value for the range (e.g. 20): "))
    while x <= 0:
        print("❌ Please enter a positive number.")
        x = int(input("Enter the maximum value for the range: "))

    print(f"\n✅ The number will be between 1 and {x}")
    print("🧠 You have 5 tries to guess it!")

    # Randomly pick a number in range
    number = random.randint(1, x)

    while tries < 5:
        guess = input("👉 Enter your guess: ")

        # Check if the input is a number
        if guess.isdigit():
            guess = int(guess)

            # Make sure the guess is within the valid range
            if guess < 1 or guess > x:
                print(f"⚠️ Please enter a number between 1 and {x}")
                continue

            # Check if guess is correct
            if guess == number:
                print("🎉 Congratulations! You guessed it right!")
                print(f"✅ You got it in {tries + 1} tries.")
                break
            elif guess < number:
                print("📉 Too low! Try again.")
            else:
                print("📈 Too high! Try again.")

            tries += 1
        else:
            print("🚫 Invalid input. Please enter a number.")

    # If the player runs out of tries
    if tries == 5 and guess != number:
        print("😢 Game Over! You’ve used all 5 tries.")
        print(f"🔍 The correct number was: {number}")

# ===== MAIN LOOP =====
while True:
    play_game()

    # Ask the user if they want to play again
    play_again = input("\n🔁 Do you want to play again? (y/n): ").lower()
    if play_again != 'y':
        print("\n🎮 Thanks for playing! Stay legendary 🔥")
        break
    else:
        print("\n🔄 Restarting the game...")
        print("🔄 Let's play again!")





