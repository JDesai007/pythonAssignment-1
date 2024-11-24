# Open the file and read its content
file_path = 'ar.txt'
file = open(file_path, 'r')
lines = file.readlines()
file.close()

# Initialize variables to compute the CGPA
total_credits = 0
total_grade_points = 0
courses = []

# Process each line in the file
for line in lines:
    parts = line.split()
    course_name = parts[0]
    credit_hours = int(parts[1])
    grade_points = float(parts[2])

    total_credits += credit_hours
    total_grade_points += credit_hours * grade_points

    # Append course details to courses list
    courses.append({
        'course': course_name,
        'credits': credit_hours,
        'points': grade_points
    })

# Calculate CGPA
cgpa = total_grade_points / total_credits

# Print the detailed academic record
print("Academic Record:")
print(f"{'Course':<10} {'Credits':<10} {'Grade Points':<15}")
for course in courses:
    print(f"{course['course']:<10} {course['credits']:<10} {course['points']:<15}")
print("\nTotal Credits Earned:", total_credits)
print("Cumulative Grade Point Average (CGPA): {:.2f}".format(cgpa))
