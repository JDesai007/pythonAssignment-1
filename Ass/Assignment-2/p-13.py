import csv
from collections import defaultdict

# Function to process the registration data
def process_registration_data(file_path):
    # Open the CSV file and read it using the csv module
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        # Using csv.DictReader to handle header and CSV format properly
        reader = csv.DictReader(file)
        
        non_students_count = 0
        iit_participants = []
        duplicates = set()
        unique_records = set()
        affiliations = defaultdict(list)
        
        for row in reader:
            # Check if this row is a duplicate (can use a unique identifier like 'name' or 'email')
            # Here, we'll assume 'name' and 'email' combined should be unique
            unique_id = (row['Name'], row['Email'])
            
            if unique_id in unique_records:
                # If the record is already processed, add it to duplicates
                duplicates.add((row['Name'], row['Email'], row['Affiliation']))
            else:
                unique_records.add(unique_id)
            
            # Check if the participant is a non-student (assuming 'Role' field contains role type)
            if row['Role'].lower() != 'student':
                non_students_count += 1
            
            # Check if the person is from an IIT
            if 'IIT' in row['Affiliation']:
                iit_participants.append((row['Name'], row['Affiliation']))
            
            # Group participants by affiliation
            affiliations[row['Affiliation']].append((row['Name'], row['Email']))

        return non_students_count, iit_participants, duplicates, affiliations

# Function to display the results
def display_results(file_path):
    non_students_count, iit_participants, duplicates, affiliations = process_registration_data(file_path)

    # 1. Display the number of non-student participants
    print(f"Number of non-students registered: {non_students_count}")
    
    # 2. Display all people registered from IITs
    print("\nParticipants from IITs:")
    for participant in iit_participants:
        print(f"Name: {participant[0]}, Affiliation: {participant[1]}")
    
    # 3. Display all duplicate records
    print("\nDuplicate records:")
    if duplicates:
        for record in duplicates:
            print(f"Name: {record[0]}, Email: {record[1]}, Affiliation: {record[2]}")
    else:
        print("No duplicate records found.")
    
    # 4. Display a list of participants grouped by their affiliations
    print("\nParticipants grouped by affiliation:")
    for affiliation, participants in affiliations.items():
        print(f"\nAffiliation: {affiliation}")
        for participant in participants:
            print(f"Name: {participant[0]}, Email: {participant[1]}")

# Example usage
file_path = 'conference_registration.csv'  # Replace with your file path
display_results(file_path)
