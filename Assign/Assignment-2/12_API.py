import json
import os

# File to store friends' information
FILE_NAME = 'friends.json'

# Initialize file with empty list if not exists
def initialize_file():
    if not os.path.isfile(FILE_NAME):
        with open(FILE_NAME, 'w') as file:
            json.dump([], file)

# Load friends' data from the file
def load_friends():
    with open(FILE_NAME, 'r') as file:
        return json.load(file)

# Save friends' data to the file
def save_friends(friends):
    with open(FILE_NAME, 'w') as file:
        json.dump(friends, file, indent=4)

# Add a new friend
def add(name, phone, github):
    initialize_file()
    friends = load_friends()
    # Check if friend already exists
    for friend in friends:
        if friend['name'] == name:
            print(f"Friend with name {name} already exists.")
            return
    friends.append({'name': name, 'phone': phone, 'github': github})
    save_friends(friends)
    print(f"Added friend {name}.")

# Remove a friend
def remove(name, phone, github):
    initialize_file()
    friends = load_friends()
    friends = [friend for friend in friends if not (friend['name'] == name and friend['phone'] == phone and friend['github'] == github)]
    save_friends(friends)
    print(f"Removed friend {name}.")

# Update phone number
def updatePhone(name, phone):
    initialize_file()
    friends = load_friends()
    for friend in friends:
        if friend['name'] == name:
            friend['phone'] = phone
            save_friends(friends)
            print(f"Updated phone number for {name}.")
            return
    print(f"Friend {name} not found.")

# Update GitHub handle
def updateGithub(name, github):
    initialize_file()
    friends = load_friends()
    for friend in friends:
        if friend['name'] == name:
            friend['github'] = github
            save_friends(friends)
            print(f"Updated GitHub handle for {name}.")
            return
    print(f"Friend {name} not found.")

# Print information of a friend
def printByName(name):
    initialize_file()
    friends = load_friends()
    for friend in friends:
        if friend['name'] == name:
            print(f"Name: {friend['name']}, Phone: {friend['phone']}, GitHub: {friend['github']}")
            return
    print(f"Friend {name} not found.")

# Print information of all friends
def printAll():
    initialize_file()
    friends = load_friends()
    if friends:
        for friend in friends:
            print(f"Name: {friend['name']}, Phone: {friend['phone']}, GitHub: {friend['github']}")
    else:
        print("No friends found.")

# Read information from the file (already covered in other functions)
def readAll():
    initialize_file()
    friends = load_friends()
    return friends
