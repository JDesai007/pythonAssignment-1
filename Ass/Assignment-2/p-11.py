def get_grade_point(grade):
    """
    Convert letter grade to grade points.
    """
    grade_points = {
        'A': 10,
        'B+': 9,
        'B': 8,
        'C+': 7,
        'C': 6,
        'D+': 5,
        'D': 4,
        'E': 0
    }
    return grade_points.get(grade.upper(), 0)  # Default to 0 for invalid grades

def compute_cgpa(input_file):
    """
    Read the academic records from the file and compute CGPA.
    """
    total_points = 0
    total_credits = 0

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            # Read each line in the file
            for line in infile:
                # Assume each line is in the format: "Course Name, Credits, Grade"
                course_details = line.strip().split(',')
                
                if len(course_details) != 3:
                    print(f"Skipping invalid line: {line.strip()}")
                    continue
                
                course_name, credits, grade = course_details
                try:
                    credits = float(credits.strip())  # Convert credits to float
                    grade = grade.strip()  # Remove any leading/trailing spaces
                    grade_point = get_grade_point(grade)
                    
                    # Calculate total points for the course
                    total_points += grade_point * credits
                    total_credits += credits
                except ValueError:
                    print(f"Invalid data in line: {line.strip()} (credits should be numeric).")
                    continue
        
        # Calculate CGPA
        if total_credits > 0:
            cgpa = total_points / total_credits
            print(f"CGPA: {cgpa:.2f}")
        else:
            print("No valid courses found to calculate CGPA.")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
input_file = 'academic_record.txt'  # Path to your academic record file
compute_cgpa(input_file)
