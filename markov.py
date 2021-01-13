"""Generate Markov text from text files."""

import sys
from random import choice

def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    file_text = open(file_path).read()

    return file_text # do we need to close? where?


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}
    words_in_text = text_string.split()
    len_gram = input("How many words would you like to use for your n-gram? ")
    len_gram = int(len_gram)

    for i in range(len(words_in_text) - len_gram):
        
        tup = tuple(words_in_text[i:i + len_gram])
        
        word_value = words_in_text[i+len_gram] 
        
        if tup not in chains:
            chains[tup] = []
            # value = []
            # chains[tup] = value.append(word_value)
        # else:
        #     for tup, value in chains.items():
        chains[tup].append(word_value)

        #Pseudocode:
        ### add word_value to tup's list
        # if tup is a new key, word_value is the first item in a list
        # if tup is an existing key, append word_value to the list

        # chains[tup] word_value[] if chains[tup] != None 

    return chains

def make_text(chains):
    """Return text from chains."""

    words = []

    # randomly get a key from our dict
    just_keys = list(chains.keys())
    key = choice(just_keys)
    
    
    # while current key exists in the dictionary:
    while chains.get(key) != None:
        # grab a random value for that key as the next 1-word
        next_word = choice(chains[key]) # will pull from key's list or value
        
        # put key    
        words.append(key[0]) #keys are all tuples, its take 
        # print(f"now, words is {words}")

        key = list(key[1::])
        key.append(next_word)
        key = tuple(key) 
        

    words.extend(key)

    # add the first word of that key into a list (words[])
    # make the second word of that key + random value into a new key
    # repeat

    return ' '.join(words)


# input_path = 'green-eggs.txt'
# in shell we will enter >> python3 markov.py filename.txt
# everything after python3 becomes tuple, we can access with sys.argv
input_path = sys.argv[1] 

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
