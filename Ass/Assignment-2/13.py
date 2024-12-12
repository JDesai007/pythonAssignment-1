import csv
from collections import defaultdict

FILE_NAME = 'conference_registration.csv'

def read_data(file_name):
   
    data = []
    try:
        with open(file_name, newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                
                if row:
                    data.append(row)
    except FileNotFoundError:
        print(f"Error: The file {file_name} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return data

def find_non_students(data):
    """Find the number of non-students registered."""
    non_students_count = sum(1 for row in data if row.get('Role', '').lower() != 'student')
    return non_students_count

def find_iit_participants(data):
    """Find all participants registered from IITs."""
    iit_participants = [row for row in data if 'IIT' in row.get('Affiliation', '')]
    return iit_participants

def find_duplicates(data):
    """Find all duplicate records based on Name, Email, and Affiliation."""
    seen = set()
    duplicates = set()
    for row in data:
        record = (row.get('Name', ''), row.get('Email', ''), row.get('Affiliation', ''))
        if record in seen:
            duplicates.add(record)
        else:
            seen.add(record)
    return duplicates

def group_by_affiliation(data):
    """Display a list of participants grouped by their affiliations."""
    affiliation_groups = defaultdict(list)
    for row in data:
        affiliation = row.get('Affiliation', 'Unknown')
        affiliation_groups[affiliation].append(row)
    return affiliation_groups

def main():
    data = read_data(FILE_NAME)
    
    if not data:
        print("No data to process.")
        return

    non_students_count = find_non_students(data)
    print(f"Number of non-students registered: {non_students_count}")
    
    iit_participants = find_iit_participants(data)
    print(f"Participants from IITs:")
    for participant in iit_participants:
        print(f"- {participant['Name']} ({participant['Email']})")
    
    duplicates = find_duplicates(data)
    print(f"Duplicate records:")
    for duplicate in duplicates:
        print(f"- {duplicate}")
    
    grouped_participants = group_by_affiliation(data)
    print(f"Participants grouped by their affiliations:")
    for affiliation, participants in grouped_participants.items():
        print(f"\nAffiliation: {affiliation}")
        for participant in participants:
            print(f"  - {participant['Name']} ({participant['Email']})")

if __name__ == "__main__":
    main()
