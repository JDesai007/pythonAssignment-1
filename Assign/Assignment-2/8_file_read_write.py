import shutil

def print_file_contents(file_path):
    """
    Print the contents of a file.
    
    :param file_path: Path to the file (str)
    """
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            print("File contents:")
            print(contents)
    except FileNotFoundError:
        print(f"Error: The file at {file_path} does not exist.")
    except IOError as e:
        print(f"Error reading file: {e}")

def copy_file(source_path, destination_path):
    """
    Copy a file from source to destination.
    
    :param source_path: Path to the source file (str)
    :param destination_path: Path to the destination file (str)
    """
    try:
        shutil.copy(source_path, destination_path)
        print(f"File copied from {source_path} to {destination_path}.")
    except FileNotFoundError:
        print(f"Error: The file at {source_path} does not exist.")
    except IOError as e:
        print(f"Error copying file: {e}")

def read_write_file(file_path, text_to_write):
    """
    Read the contents of a file and then write new text to it.
    
    :param file_path: Path to the file (str)
    :param text_to_write: Text to write to the file (str)
    """
    try:
        # Reading the file
        with open(file_path, 'r') as file:
            contents = file.read()
            print("Current file contents:")
            print(contents)
        
        # Writing to the file
        with open(file_path, 'a') as file:
            file.write(text_to_write)
            print(f"Text appended to {file_path}.")
        
    except FileNotFoundError:
        print(f"Error: The file at {file_path} does not exist.")
    except IOError as e:
        print(f"Error reading/writing file: {e}")

# Example usage
if __name__ == "__main__":
    # Replace with actual file paths
    file_path = 'example.txt'
    copied_file_path = 'example_copy.txt'
    text_to_append = '\nThis is some new text appended to the file.'

    # Print file contents
    print_file_contents(file_path)

    # Copy a file
    copy_file(file_path, copied_file_path)

    # Read and write to the file
    read_write_file(file_path, text_to_append)
