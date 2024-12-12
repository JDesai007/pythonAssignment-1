def read_academic_records(file_path):
 
    records = []
    try:
        with open(file_path, 'r') as file:
            for line in file:
               
                line = line.strip()
                if line:
                    parts = line.split(',')
                    if len(parts) == 3:
                        course_name = parts[0]
                        try:
                            credits = float(parts[1])
                            points = float(parts[2])
                            records.append((course_name, credits, points))
                        except ValueError:
                            print(f"Skipping invalid line: {line}")
    except FileNotFoundError:
        print(f"Error: The file at {file_path} does not exist.")
    except IOError as e:
        print(f"Error reading file: {e}")
    return records

def compute_cgpa(records):

    total_points = 0
    total_credits = 0
    
    for _, credits, points in records:
        total_points += credits * points
        total_credits += credits
    
    if total_credits == 0:
        return 0 
    
    return total_points / total_credits

def main():
   
    file_path = 'academic_record.txt'  
    records = read_academic_records(file_path)
    
    if not records:
        print("No records found or failed to read the file.")
        return
    
    cgpa = compute_cgpa(records)
    
    print("Academic Records:")
    for record in records:
        print(f"Course: {record[0]}, Credits: {record[1]}, Points: {record[2]}")
    
    print(f"\nComputed CGPA: {cgpa:.2f}")

if __name__ == "__main__":
    main()
