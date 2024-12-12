import json

file_path = 'friend.json'

def read_all():
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def write_all(data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def add_friend(name, phone, github):
    data = read_all()
    data[name] = {'phone': phone, 'github': github}
    write_all(data)
    print(f"Friend {name} added successfully.")

def remove_friend(name):
    data = read_all()
    if name in data:
        del data[name]
        write_all(data)
        print(f"Friend {name} removed successfully.")
    else:
        print(f"Friend {name} not found.")

def update_phone(name, phone):
    data = read_all()
    if name in data:
        data[name]['phone'] = phone
        write_all(data)
        print(f"Phone number for {name} updated successfully.")
    else:
        print(f"Friend {name} not found.")

def update_github(name, github):
    data = read_all()
    if name in data:
        data[name]['github'] = github
        write_all(data)
        print(f"GitHub username for {name} updated successfully.")
    else:
        print(f"Friend {name} not found.")

def print_by_name(name):
    data = read_all()
    if name in data:
        print(f"Name: {name}")
        print(f"Phone: {data[name]['phone']}")
        print(f"GitHub: {data[name]['github']}")
    else:
        print(f"Friend {name} not found.")

def print_all():
    data = read_all()
    if data:
        for name, info in data.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"GitHub: {info['github']}")
            print("---------")
    else:
        print("No friends found.")

add_friend('Alice', '123-456-7890', 'alice_github')
add_friend('Bob', '987-654-3210', 'bob_github')
update_phone('Alice', '111-222-3333')
update_github('Bob', 'new_bob_github')
print_by_name('Alice')
print_all()
remove_friend('Alice')
print_all()
