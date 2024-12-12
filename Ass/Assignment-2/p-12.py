import os
import json

FILE_NAME = 'friends_data.txt'

def readAll():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return json.load(f)
    return []

def saveAll(friends_list):
    with open(FILE_NAME, 'w') as f:
        json.dump(friends_list, f, indent=4)


def add(name, phone, github):
    friends = readAll()
    new_friend = {'name': name, 'phone': phone, 'github': github}
    friends.append(new_friend)
    saveAll(friends)
    print(f"Added friend: {name}")

def remove(name=None, phone=None, github=None):
    friends = readAll()
    friends_to_remove = [f for f in friends if (f['name'] == name or f['phone'] == phone or f['github'] == github)]
    if friends_to_remove:
        friends = [f for f in friends if not (f['name'] == name or f['phone'] == phone or f['github'] == github)]
        saveAll(friends)
        print(f"Removed friend: {friends_to_remove[0]['name']}")
    else:
        print("Friend not found.")


def updatePhone(name, phone):
    friends = readAll()
    friend_found = False
    for friend in friends:
        if friend['name'] == name:
            friend['phone'] = phone
            friend_found = True
            break
    if friend_found:
        saveAll(friends)
        print(f"Updated phone number for {name}.")
    else:
        print(f"Friend {name} not found.")


def updateGithub(name, github):
    friends = readAll()
    friend_found = False
    for friend in friends:
        if friend['name'] == name:
            friend['github'] = github
            friend_found = True
            break
    if friend_found:
        saveAll(friends)
        print(f"Updated GitHub handle for {name}.")
    else:
        print(f"Friend {name} not found.")

def printByName(name):
    friends = readAll()
    friend_found = False
    for friend in friends:
        if friend['name'] == name:
            print(f"Friend: {friend['name']}, Phone: {friend['phone']}, GitHub: {friend['github']}")
            friend_found = True
            break
    if not friend_found:
        print(f"Friend {name} not found.")


def printAll():
    friends = readAll()
    if friends:
        for friend in friends:
            print(f"Friend: {friend['name']}, Phone: {friend['phone']}, GitHub: {friend['github']}")
    else:
        print("No friends available.")


if __name__ == '__main__':
 
    add('Alice', '1234567890', 'alice_github')
    add('Bob', '0987654321', 'bob_github')
    printAll()
    printByName('Alice')
    updatePhone('Alice', '1112223333')
    updateGithub('Bob', 'bob_updated')
    remove(name='Alice')
    printAll()
