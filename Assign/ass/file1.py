file_path = 'files2.txt'
text_to_add = 'This is additional text.'

file = open(file_path, 'r+')
contents = file.read()
print("Original contents:")
print(contents)

file.write("\n" + text_to_add)
file.close()
print(f"\nText '{text_to_add}' added to the file.")