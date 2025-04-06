"""
Hangman Game (One File Version with 150 Custom Words)
"""

import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


import random

WORDS = [
    "PYTHON", "HANGMAN", "TERMINAL", "PARROT", "UBUNTU", "LINUX", "HACKING", "GITHUB", "REPO", "COMMIT",
    "BRANCH", "MERGE", "CLONE", "PULL", "PUSH", "STATUS", "FORK", "ISSUE", "BUG", "FIX", "FEATURE",
    "RELEASE", "VERSION", "SCRIPT", "FUNCTION", "LOOP", "VARIABLE", "ARRAY", "STRING", "INTEGER", "FLOAT",
    "LIBRARY", "PACKAGE", "IMPORT", "EXPORT", "DEBUG", "COMPILE", "EXECUTE", "ENCRYPT", "DECRYPT", "CIPHER",
    "TOKEN", "COOKIE", "SESSION", "REQUEST", "RESPONSE", "SERVER", "CLIENT", "BACKEND", "FRONTEND", "DATABASE",
    "QUERY", "OBJECT", "CLASS", "METHOD", "SYNTAX", "EXCEPTION", "TRY", "EXCEPT", "FINALLY", "RAISE",
    "ASSERT", "IDE", "EDITOR", "VSCODE", "NOTEBOOK", "BASH", "SHELL", "ROOT", "SUDO", "USER",
    "ADMIN", "NMAP", "SQLMAP", "PROXY", "PAYLOAD", "XSS", "CSRF", "BUFFER", "MALWARE", "PHISHING",
    "ATTACK", "FIREWALL", "HASH", "CHECKSUM", "ALGORITHM", "BINARY", "HEXADECIMAL", "BOOLEAN", "INPUT", "OUTPUT",
    "PRINT", "OPEN", "READ", "WRITE", "FILE", "PATH", "OS", "SYSTEM", "PLATFORM", "THREAD",
    "ASYNC", "AWAIT", "LAMBDA", "LIST", "DICT", "TUPLE", "JSON", "HTTP", "HTTPS", "SSL",
    "CERT", "KEY", "AUTH", "MODEL", "DATASET", "NEURAL", "NETWORK", "TRAIN", "TEST", "ACCURACY",
    "VISION", "LANGUAGE", "NLP", "TRANSFORMER", "CHATBOT", "PROMPT", "RESPONSE", "SHADE", "JOURNAL", "DAILY",
    "NOTE", "SAVE", "DELETE", "UPDATE", "TASK", "TODO", "GOAL", "MOTIVATE", "FOCUS", "STUDY"
]

HANGMAN_PICS = [
    """
     +---+
         |
         |
         |
        ===""", """
     +---+
     O   |
         |
         |
        ===""", """
     +---+
     O   |
     |   |
         |
        ===""", """
     +---+
     O   |
    /|   |
         |
        ===""", """
     +---+
     O   |
    /|\\  |
         |
        ===""", """
     +---+
     O   |
    /|\\  |
    /    |
        ===""", """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

def display_board(stage, guessed, word, level, score):
    print(HANGMAN_PICS[stage])
    print(f"\n🎯 Level: {level} | 🧠 Score: {score}")
    print("Word: ", end="")
    for letter in word:
        print(letter if letter in guessed else "_", end=" ")
    print("\nGuessed Letters:", " ".join(sorted(guessed)))

def play_hangman():
    level = 1
    score = 0
    max_wrong = len(HANGMAN_PICS) - 1

    while True:
        word = random.choice(WORDS).upper()
        guessed = set()
        wrong = 0

        print("\n🎮 NEW ROUND!")
        print(f"➡️ Level {level} | ✅ Score: {score}")

        while wrong < max_wrong:
            display_board(wrong, guessed, word, level, score)
            guess = input("Guess a letter: ").upper()

            if not guess.isalpha() or len(guess) != 1:
                print("⛔ Please enter a single letter.")
                continue
            if guess in guessed:
                print("⚠️ Already guessed.")
                continue

            guessed.add(guess)

            if guess not in word:
                wrong += 1
                print("❌ Incorrect!")
            else:
                print("✅ Correct!")

            if all(letter in guessed for letter in word):
                score += 10
                level += 1
                print(f"\n🎉 You guessed it! The word was: {word}")
                break
        else:
            display_board(wrong, guessed, word, level, score)
            print(f"\n💀 Game Over! The word was: {word}")
            print(f"🏆 Final Score: {score} | Level Reached: {level}")
            break

if __name__ == "__main__":
    print("🎉 Welcome to the HANGMAN 150 Game!")
    play_hangman()
