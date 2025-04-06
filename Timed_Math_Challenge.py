import random
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-', '*'])
    question = f"{a} {op} {b}"
    answer = eval(question)
    return question, answer

def math_challenge(duration=30):
    print(f"🧠 Timed Math Challenge! You have {duration} seconds. Solve as many as you can!")
    input("Press Enter to start...")
    score = 0
    total = 0
    start_time = time.time()

    while time.time() - start_time < duration:
        question, correct = generate_question()
        try:
            user_input = input(f"{question} = ")
            if time.time() - start_time >= duration:
                break
            if int(user_input) == correct:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Wrong! The correct answer was {correct}")
            total += 1
        except ValueError:
            print("⚠️ Invalid input. Skipping.")
    
    print("\n⏰ Time's up!")
    print(f"✅ You got {score} out of {total} correct.")

# Run the challenge
math_challenge(duration=30)
# This code implements a timed math challenge where the user has to solve as many math problems as possible within a given time limit.
# The user is presented with random math questions, and their score is calculated based on the number of correct answers.
# The game ends when the time is up, and the user is shown their score. 