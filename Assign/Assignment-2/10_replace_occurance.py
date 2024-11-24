def read_file(file_path):
    """
    Read the contents of a file.
    
    :param file_path: Path to the file (str)
    :return: Contents of the file as a string (str)
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: The file at {file_path} does not exist.")
        return ""
    except IOError as e:
        print(f"Error reading file: {e}")
        return ""

def write_file(file_path, content):
    """
    Write content to a file.
    
    :param file_path: Path to the file (str)
    :param content: Content to write to the file (str)
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        print(f"Error writing file: {e}")

def replace_word(file_path, old_word, new_word):
    """
    Replace all occurrences of a word in a file.
    
    :param file_path: Path to the file (str)
    :param old_word: Word to replace (str)
    :param new_word: Word to replace with (str)
    """
    # Read the file
    text = read_file(file_path)
    if not text:
        return
    
    # Replace the old word with the new word
    updated_text = text.replace(old_word, new_word)
    
    # Write the updated content back to the file
    write_file(file_path, updated_text)
    
    print(f"All occurrences of '{old_word}' have been replaced with '{new_word}'.")

# Example usage
if __name__ == "__main__":
    file_path = 'sample.txt'  # Replace with your file path
    replace_word(file_path, 'gujarat', 'gujrat')
