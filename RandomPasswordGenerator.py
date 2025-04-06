import random
import string

def generate_password(length):

    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


while True:

    length  = int(input("Enter password length: "))
    print("Generated Password:", generate_password(length))


    choice = input("Generate another password? (yes/no)").lower
    if choice != "no" :
        print("Goodbye!")
        break

