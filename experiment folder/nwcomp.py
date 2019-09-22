import string
import os


def get_filename():
    """Function to get the file name from user input"""
    # Infinite loop to ask the user for a file name that must be valid in order to break the loop.
    while True:
        # Ask the user for a file name.
        filename = input('Please input text file name in current directory: \n')
        # Append .txt extension if not provided.
        filename = filename if filename.endswith('.txt') else '{}.txt'.format(filename)
        # Test if the file exist and return it, print an error and continue loop if not.
        if os.path.isfile(filename):
            return filename
        else:
            print('No Such text file in current directory: {}'.format(filename))


def comp(full_text):
    # Making a translation table to get rid of punctuation and keep only letters.
    table = str.maketrans(string.punctuation, ' ' * len(string.punctuation))
    only_words = full_text.translate(table)
    # Create a sorted list of unique elements.
    word_list = sorted(set(only_words.split()))
    # Replace every word of the original text by it's index in the word list.
    for index, word in enumerate(word_list):
        full_text = full_text.replace(word, '{{{}}}'.format(index))  # Double brackets are ignored by .format()
    file_out = '{}@***{}***'.format(full_text, '|'.join(word_list))
    
    return(file_out)


def decomp(file_in):

    full_text = file_in.split('@')
        # Remove the last line of the text and convert it to a sorted list of the reference words.
    reference = sorted(full_text.pop(-1).strip('*').split('|'))
    # Print the full text replacing the indexes by the corresponding word in the list.
    return(''.join(full_text).format(*reference))
