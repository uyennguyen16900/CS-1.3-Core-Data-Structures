#!python

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    # return linear_search_iterative(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    # implement linear search recursively here
    if array[0] == item:
        return index
    elif len(array) > 1:
        return linear_search_recursive(array[1:], item, index+1)
    else:
        return None
    # once implemented, change linear_search to call linear_search_recursive
    # to verify that your recursive implementation passes all tests


def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    return binary_search_iterative(array, item)
    # return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    # implement binary search iteratively
    # change binary_search to call binary_search_iterative
    # to verify that your iterative implementation passes all tests
    right = len(array) - 1
    left = 0
    mid = len(array) // 2
    while len(array) > 1 and array[mid] != item:
        if array[mid] > item:
            array = array[:mid]
            right = right - mid - 1

        else:
            array = array[mid+1:]
            left = left + mid + 1

        mid = len(array) // 2

    if array[mid] == item:
        return (right + left) // 2
    else:
        return None


def binary_search_recursive(array, item, left=None, right=None):
    # implement binary search recursively here
    if left is None and right is None:
        right = len(array) - 1
        left = 0
    mid = len(array) // 2
    if left > right:
        return None
    elif array[mid] == item:
        return (left + right) // 2
    elif array[mid] > item:
        return binary_search_recursive(array[:mid], item, left, right-mid-1)
    else:
        return binary_search_recursive(array[mid+1:], item, left+mid+1, right)


    # once implemented, change binary_search to call binary_search_recursive
    # to verify that your recursive implementation passes all tests

if __name__ == '__main__':
    array = [1,3,5,2,6,8,9,4]
    ordered_array = [1,3,4,7,8,13,20]
    # print(linear_search_recursive(array, 4, index=0))
    print(binary_search_recursive(ordered_array, 8))
    # print(binary_search_iterative(ordered_array, 20))
