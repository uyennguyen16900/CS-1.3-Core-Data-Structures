from stack import *
from queue import *
import collections

# double-ended queue
class Deque(object):

    def __init__(self, iterable=None):
        """Implement a deque using two stacks"""
        # Initialize a new linked list to store the items
        self.front_stack = LinkedStack()
        self.back_stack = ArrayStack()
        # if iterable is not None:
        #     for item in iterable:
        #         self.enqueue(item)
        self._display_stack()

    def size(self):
        # reverse_back_stack.push()
        return self.front_stack().length() + self.back_stack().length()

    def push_front(self, item):
        """Push item to the front of front_stack"""
        self.front_stack.push(item)

    def push_back(self, item):
        """Push item to the back of back_stack"""
        self.back_stack.push(item)

    def is_empty(self):
        """Check if stack is empty"""
        return self.size() == 0

    def pop_front(self):
        """Pop item from the front of front_stack"""
        if self.is_empty():
            raise ValueError('The queue is empty.')
        else:
            self.front_stack.pop()

    def pop_back(self):
        """Pop item from the back of back_stack"""
        if self.is_empty():
            raise ValueError('The queue is empty.')
        else:
            self.back_stack.pop()

    def _display_stack(self):
        return self.front_stack + self.back_stack

def test_deque():
    print('From the right:')
    d = Deque()
    d.push_back('b')
    d.push_back('c')
    d.push_back('d')
    d.push_back('e')
    d.push_front('a')

    while True:
        try:
            print(d.pop_back())
        except IndexError:
            break

    print('\nFrom the left:')
    d = Deque()
    d.push_back('b')
    d.push_back('c')
    d.push_back('d')
    d.push_back('e')
    d.push_front('a')

    while True:
        try:
            print(d.pop_front())
        except IndexError:
            break

if __name__ == '__main__':
    test_deque()
