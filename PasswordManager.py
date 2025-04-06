import os
import json
from cryptography.fernet import Fernet
import random
import string

DATA_FILE = "vault.json"
KEY_FILE = "secret.key"

# 🔐 Key functions
def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

fernet = Fernet(load_key())

# 🔐 File functions
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)

# 🔐 Encryption helpers
def encrypt(text):
    return fernet.encrypt(text.encode()).decode()

def decrypt(text):
    return fernet.decrypt(text.encode()).decode()

# 🧠 Password Generator
def generate_password(length=12):
    chars = string.ascii_letters + string.digits + "!@#$%^&*()-_=+"
    return ''.join(random.choice(chars) for _ in range(length))

# 🛠️ Core Functions
def add_password(data):
    site = input("Site name: ")
    username = input("Username: ")
    password = input("Password (leave empty to generate): ")

    if not password:
        password = generate_password()
        print(f"Generated password: {password}")

    data[site] = {
        "username": encrypt(username),
        "password": encrypt(password)
    }
    save_data(data)
    print("✅ Password saved.")

def view_passwords(data):
    if not data:
        print("❌ No entries found.")
        return
    for site, creds in data.items():
        print(f"\n🔐 {site}")
        print(f"   Username: {decrypt(creds['username'])}")
        print(f"   Password: {decrypt(creds['password'])}")

def search_password(data):
    site = input("Search site: ")
    if site in data:
        creds = data[site]
        print(f"\n🔎 {site}")
        print(f"   Username: {decrypt(creds['username'])}")
        print(f"   Password: {decrypt(creds['password'])}")
    else:
        print("❌ Not found.")

# 📋 Main Menu
def main():
    data = load_data()
    while True:
        print("\n🔐 Encrypted Password Manager")
        print("1. Add Password")
        print("2. View All")
        print("3. Search")
        print("4. Exit")
        choice = input("Choose (1-4): ")

        if choice == "1":
            add_password(data)
        elif choice == "2":
            view_passwords(data)
        elif choice == "3":
            search_password(data)
        elif choice == "4":
            print("👋 Bye! Stay secure.")
            break
        else:
            print("❗ Invalid choice.")

if __name__ == "__main__":
    main()
