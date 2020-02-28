import unittest
from set import TreeSet

class TreeSetTest(unittest.TestCase):

    def test_init(self):
        s = TreeSet([1])
        assert s.size == s.length()

    def test_duplicate(self):
        s = TreeSet([1,2])
        with self.assertRaises(ValueError):
            s.add(1)

    def test_contains(self):
        s = TreeSet()
        s.add('A')
        s.add('B')
        s.add('C')
        assert s.contains('A') is True
        assert s.contains('B') is True
        assert s.contains('D') is False
        s.remove('A')
        assert s.contains('A') is False
        assert s.size == 2

    def test_union(self):
        s1 = TreeSet([1,2,3,4])
        s2 = TreeSet([4,2,5,1])
        union_set = s1.union(s2)
        assert union_set.contains(1) is True
        assert union_set.contains(2) is True
        assert union_set.contains(4) is True
        assert union_set.contains(3) is True
        assert union_set.contains(5) is True

        assert union_set.contains(6) is False

    def test_difference(self):
        s1 = TreeSet(['A', 'B', 'D'])
        s2 = TreeSet(['A', 'B', 'C'])
        difference_set = s2.difference(s1)
        assert difference_set.size == 2
        assert difference_set.contains('D')
        assert difference_set.contains('C')

    def test_subset(self):
        s1 = TreeSet([1,2,3,4,5])
        s2 = TreeSet([1,2,3,4,5,6])
        assert s1.is_subset(s2) is True
        assert s2.is_subset(s1) is False


if __name__ == '__main__':
    unittest.main()
