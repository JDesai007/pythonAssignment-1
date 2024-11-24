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

def split_and_join_text(source_file, destination_file):
    """
    Split text into words and join them to form sentences, then write to a new file.
    
    :param source_file: Path to the source file (str)
    :param destination_file: Path to the destination file (str)
    """
    text = read_file(source_file)
    if not text:
        return

    # Split text into words
    words = text.split()

    # Join words to form sentences
    sentences = []
    sentence = []
    for word in words:
        sentence.append(word)
        if word.endswith(('.', '!', '?')):
            sentences.append(' '.join(sentence))
            sentence = []

    if sentence:
        sentences.append(' '.join(sentence))

    # Join sentences into final content
    final_content = '\n'.join(sentences)

    # Write to destination file
    write_file(destination_file, final_content)

    print(f"Text has been processed and written to {destination_file}")

# Example usage
if __name__ == "__main__":
    source_file_path = 'source.txt'
    destination_file_path = 'destination.txt'
    
    split_and_join_text(source_file_path, destination_file_path)
