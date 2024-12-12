# Function to read text from a file and split it into words
def split_text_to_words(input_file):
    file = open(input_file, 'r')
    text = file.read()
    file.close()
    words = text.split()
    return words

# File path
input_file = 'files.txt'

# Split text from input file into words
words = split_text_to_words(input_file)

print(f'The words in the file {input_file} are: {words}')
# Function to read text from a file and split it into words


# Function to join words into a sentence and write to another file
def join_words_to_sentence(words, output_file):
    file = open(output_file, 'w')
    sentence = ' '.join(words)
    file.write(sentence)
    file.close()

# File paths
input_file = 'files.txt'
output_file = 'output.txt'

# Split text from input file into words
words = split_text_to_words(input_file)

# Join words into a sentence and write to output file
join_words_to_sentence(words, output_file)

print(f'Text from {input_file} has been split into words and written as a sentence in {output_file}.')

