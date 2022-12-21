"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    file = open(file_path).read()
    new_string = " ".join(file.split())

    return new_string


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

    text_string = text_string.split()
    for index in range(0, len(text_string) - 2):
        dict_key = (text_string[index], text_string[index + 1])
        dict_value = [text_string[index + 2]]
        # if dict_key in chains.keys():
        #     chains[dict_key].append(dict_value)
        # else:
        #     chains[dict_key] = [dict_value]
        chains[dict_key] = chains.get(dict_key, []) + dict_value

    return chains


def make_text(chains):
    """Return text from chains."""

    words = []

    random_key = choice(list(chains.keys()))
    random_value = choice(chains[random_key])
    words += list(random_key)
    words.append(random_value)

    new_key = tuple(words[-2:])
    while new_key in chains.keys():
        words.append(choice(chains[new_key]))
        new_key = tuple(words[-2:])

    return ' '.join(words)


input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(f"Generated random text is \n{random_text}")
