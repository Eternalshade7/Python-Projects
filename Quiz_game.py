print("Welcome to the Quiz Game!")
playing = input("Do you want to play? (yes/no): ")

if playing.lower() != "yes":
    quit()

print("Great! Let's start the game.")
score = 0
print("You will be asked a series of questions. Type your answer and press Enter.\n")

answer = input("1. What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'central processing unit'")

answer = input("2. What does GPU stand for? ").lower()
if answer == "graphics processing unit":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'graphics processing unit'")

answer = input("3. What does RAM stand for? ").lower()
if answer == "random access memory":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'random access memory'")

answer = input("4. What does ROM stand for? ").lower()
if answer == "read only memory":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'read only memory'")

answer = input("5. What does PSU stand for? ").lower()
if answer == "power supply unit":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'power supply unit'")

answer = input("6. What does SSD stand for? ").lower()
if answer == "solid state drive":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'solid state drive'")

answer = input("7. What does HDD stand for? ").lower()
if answer == "hard disk drive":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'hard disk drive'")

answer = input("8. What does USB stand for? ").lower()
if answer == "universal serial bus":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'universal serial bus'")

answer = input("9. What does HDMI stand for? ").lower()
if answer == "high definition multimedia interface":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'high definition multimedia interface'")

answer = input("10. What does VGA stand for? ").lower()
if answer == "video graphics array":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'video graphics array'")

answer = input("11. What does DVI stand for? ").lower()
if answer == "digital visual interface":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'digital visual interface'")

answer = input("12. What does LAN stand for? ").lower()
if answer == "local area network":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'local area network'")

answer = input("13. What does WAN stand for? ").lower()
if answer == "wide area network":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'wide area network'")

answer = input("14. What does WLAN stand for? ").lower()
if answer == "wireless local area network":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'wireless local area network'")

answer = input("15. What does VPN stand for? ").lower()
if answer == "virtual private network":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'virtual private network'")

answer = input("16. What does IP stand for? ").lower()
if answer == "internet protocol":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'internet protocol'")

answer = input("17. What does URL stand for? ").lower()
if answer == "uniform resource locator":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'uniform resource locator'")

answer = input("18. What does HTTP stand for? ").lower()
if answer == "hypertext transfer protocol":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'hypertext transfer protocol'")

answer = input("19. What does HTTPS stand for? ").lower()
if answer == "hypertext transfer protocol secure":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'hypertext transfer protocol secure'")

answer = input("20. What does FTP stand for? ").lower()
if answer == "file transfer protocol":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'file transfer protocol'")

answer = input("21. What does SFTP stand for? ").lower()
if answer == "secure file transfer protocol":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'secure file transfer protocol'")

answer = input("22. What does SSH stand for? ").lower()
if answer == "secure shell":
    print("Correct! You got it right.")
    score += 1
else:
    print("Incorrect! The correct answer is 'secure shell'")

# Final Score
print(f"\nYou got {score} out of 22 correct!")
print("Thank you for playing the Quiz Game!")
print("Goodbye!")
# End of the Quiz Game
# This is a simple quiz game that tests the user's knowledge on computer hardware and networking terms.
# The game consists of 22 questions, and the user is prompted to answer each question.  
                                