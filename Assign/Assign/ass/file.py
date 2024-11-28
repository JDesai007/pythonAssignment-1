
file = open('files.txt', 'r')
contents = file.read()
print(contents)
file.close()
source_path = 'files.txt'
destination_path = 'filesdest.txt'

src_file = open(source_path, 'r')
contents = src_file.read()
src_file.close()

dest_file = open(destination_path, 'w')
dest_file.write(contents)
dest_file.close()

print(f"File copied from {source_path} to {destination_path}")

