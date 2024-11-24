# Define an empty dictionary to store course records
courses = {}

def add_course(course_name, credits, points):
    
    if credits <= 0 or points < 0:
        raise ValueError("Credits must be positive and points cannot be negative.")
    courses[course_name] = {'credits': credits, 'points': points}

def drop_course(course_name):
  
    if course_name in courses:
        del courses[course_name]
    else:
        print(f"Course '{course_name}' not found.")

def print_record():
  
    if not courses:
        print("No courses recorded.")
        return

    print(f"{'Course Name':<20} {'Credits':<10} {'Points':<10}")
    print("_"*40)
    for course_name, details in courses.items():
        print(f"{course_name:<20} {details['credits']:<10} {details['points']:<10}")

def calculate_cgpa():
  
    total_credits = sum(details['credits'] for details in courses.values())
    weighted_points = sum(details['credits'] * details['points'] for details in courses.values())
    
    if total_credits == 0:
        return 0.0
    
    return weighted_points / total_credits

# Example usage
if __name__ == "__main__":
    # Adding courses
    add_course("Python", 3, 9)
    add_course("DBMS", 4, 12)
    add_course("Java", 5, 7)
    add_course("DS", 3, 12)
    
    # Printing the record
    print("Academic Record:")
    print()
    print_record()
    
    # Calculating CGPA
    print(f"CGPA: {calculate_cgpa():.2f}")

    # Dropping a course
    drop_course("Python")
    
    # Printing the updated record
    print()
    print("\nUpdated Academic Record:")
    print()
    print_record()
    
    # Recalculating CGPA
    print(f"Updated CGPA: {calculate_cgpa():.2f}")
