import json
import hashlib

def sign_up():
    try:
        # Open the file in read mode to load existing user data
        with open('users.json', 'r') as file:
            # Check if the file is empty
            file_content = file.read().strip()
            if not file_content:
                data = {}  # Initialize an empty dictionary if the file is empty
            else:
                data = json.loads(file_content)  # Load existing data from the file
    except FileNotFoundError:
        # If the file doesn't exist, initialize an empty dictionary
        data = {}

    username = input('Enter your username: ')
    password = input('Enter your password: ')

    # Check if the username already exists
    if username in data:
        print("Username already exists. Please choose a different one.")
        return

    # Hash the password before storing
    hashed_password = hashlib.sha256(password.encode()).hexdigest()

    # Add the username and hashed password to the data
    data[username] = hashed_password

    # Write the updated data back to the file
    with open('users.json', 'w') as file:
        json.dump(data, file)
        print("Sign up successful.")

sign_up()
