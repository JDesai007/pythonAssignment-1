# Define the file paths
file_path = 'example.txt'
temp_file_path = 'temp_example.txt'

# Open the source file and a temporary file
file = open(file_path, 'r')
temp_file = open(temp_file_path, 'w')

# Read each line, replace occurrences, and write to the temporary file
for line in file:
    updated_line = line.replace('Gujarat', 'Gujrat')
    temp_file.write(updated_line)

# Close the files
file.close()
temp_file.close()

# Replace the original file with the updated file
import os
os.remove(file_path)
os.rename(temp_file_path, file_path)

print(f"All occurrences of 'Gujarat' have been replaced with 'Gujrat' in {file_path}")
