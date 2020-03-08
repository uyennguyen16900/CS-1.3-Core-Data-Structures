from search import binary_search
from binarytree import BinarySearchTree
from random import shuffle
from hashtable import HashTable

def get_permutations(string):
    """Return all permutations of the string"""
    if len(string) == 0:
        return []
    elif len(string) == 1:
        return string
    else:
        ls = []
        for i in range(len(string)):
            starting_letter = string[i]
            rest = string[:i] + string[i+1:]
            for j in get_permutations(rest):
                ls.append(starting_letter+j)

    return ls


def get_words():
    # get words from a file
    file = open('/usr/share/dict/words','r')
    words = file.read().split()
    file.close()
    shuffle(words)
    tree_words = BinarySearchTree(words)
    return tree_words


def solve_jumble_word(letters):
    """Return a hash table with each letter is a key and the result is its value"""
    words = get_words()
    # create a hash table to store all the letters with their final result(s)
    results = HashTable(len(letters))
    for letter in letters:
        result = []
        perms = get_permutations(letter)
        for element in perms:
            word = words.search(element)
            if word is not None and word not in result:
                result.append(word)
        results.set(letter, result)

    return results


if __name__ == "__main__":
    jumble_words = ['tefon', 'sokik', 'niumem', 'siconu', 'rca']
    solved_words = solve_jumble_word(jumble_words)
    for i in range(len(jumble_words)):
        print(f'The answer of {jumble_words[i]} is {solved_words.get(jumble_words[i])}')
