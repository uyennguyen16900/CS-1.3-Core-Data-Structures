from binarytree import BinarySearchTree


class TreeSet:
    def __init__(self, elements=None):
        """initialize a new empty set structure, and add each element if a sequence is given
        size - property that tracks the number of elements in constant time"""
        self.tree = BinarySearchTree()
        self.size = 0
        if elements is not None:
            for element in elements:
                self.add(element)

    def length(self):
        return self.size

    def contains(self, element):
        """return a boolean indicating whether element is in this set"""
        if self.tree.contains(element):
            return True
        # return self.tree.contains(element) is not None
        return False

    def add(self, element):
        """add element to this set, if not present already"""
        if self.contains(element):
            raise ValueError('Cannot add element to set again: {}'.format(element))
        else:
            self.tree.insert(element)
            self.size += 1

    def remove(self, element):
        """remove element from this set, if present, or else raise KeyError"""
        self.tree.delete(element)
        self.size -= 1

    def union(self, other_set):
        """return a new set that is the union of this set and other_set"""
        union_set = self.tree.items_in_order()
        for element in other_set.tree.items_in_order():
            if element not in union_set:
                union_set.append(element)

        return TreeSet(union_set)

    def intersection(self, other_set):
        """return a new set that is the intersection of this set and other_set"""
        intersection_set = TreeSet()
        for element in self.tree.items_in_order():
            if other_set.contains(element):
                intersection_set.add(element)

        return intersection_set

    def difference(self, other_set):
        """return a new set that is the difference of this set and other_set"""
        difference_set = TreeSet()
        for element in other_set.tree.items_in_order():
            if self.tree.contains(element) is False:
                difference_set.add(element)

        for element in self.tree.items_in_order():
            if other_set.contains(element) is False:
                difference_set.add(element)


        return difference_set

    def is_subset(self, other_set):
        """return a boolean indicating whether this set is a subset of other_set"""
        if other_set.size < self.size:
            return False

        for element in self.tree.items_in_order():
            if other_set.contains(element) is False:
                return False

        return True

Set = TreeSet

def test_treeset():
    items_1 = ['A', 'B', 'C']
    items_2 = ['B', 'C', 'D']
    s1 = TreeSet()
    s2 = TreeSet()

    for item in items_1:
        s1.add(item)

    for item in items_2:
        s2.add(item)

    print(s1.union(s2))




if __name__ == '__main__':
    test_treeset()
