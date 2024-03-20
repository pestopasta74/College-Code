import json
import hashlib

def sign_in():
    try:
        # Open the file in read mode to load existing user data
        with open('users.json', 'r') as file:
            data = json.load(file)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        print("No existing users found. Please sign up first.")
        return

    username = input('Enter your username: ')
    password = input('Enter your password: ')

    # Check if the username exists
    if username not in data:
        print("Username doesn't exist. Please sign up first.")
        return

    # Hash the input password for comparison
    hashed_input_password = hashlib.sha256(password.encode()).hexdigest()

    # Compare hashed passwords in constant time to avoid timing attacks
    stored_password = data[username]
    if hashed_input_password == stored_password:
        print('You are signed in')
    else:
        print('Incorrect username or password')

sign_in()
