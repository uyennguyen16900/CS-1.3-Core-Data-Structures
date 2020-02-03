#!python
def find_index_contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text and index of the first occurence."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    for i in range(len(text)-len(pattern)+1):
        if text[i] == pattern[0]:
            if text[i+1:i+len(pattern)] == pattern[1:]:
                return True, i

    return False, None

def contains(text, pattern):
    # return find_index_contains(text, pattern)[0]
    """Return a boolean indicating whether pattern occurs in text and index of the first occurence."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement contains here (iteratively and/or recursively)
    if pattern == '':
        return True

    return find_index_contains(text, pattern)[0]

def contains_recursively(text, pattern):
    """Return a boolean indicating whether pattern occurs in text and index of the first occurence."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':
        return 0

    if len(text) < len(pattern):
        return False
    elif text[:len(pattern)] == pattern:
        return True
    else:
        return contains_recursively(text[1:], pattern)


def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_index here (iteratively and/or recursively)
    if pattern == '':
        return 0
    return find_index_contains(text, pattern)[1]

def find_index_recursively(text, pattern, index=0):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

    if pattern == '':
        return 0

    if len(text) < len(pattern):
        return None
    elif text[:len(pattern)] == pattern:
        return index
    else:
        return find_index_recursively(text[1:], pattern, index+1)

def find_all_indexes(text, pattern):
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    # length = len(text)
    if pattern == '':
        return [i for i in range(len(text))]
    else:
        list = []
        count = 0
        bool, index = find_index_contains(text, pattern)
        s = text

        while bool:
            count += index
            list.append(count)
            s = s[index+1:]
            bool, index = find_index_contains(s, pattern)
            count += 1
        return list

def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    # main()
    test_string_algorithms('abra cadabra', 'abra')
