from stack import Stack
from queue import Queue

# double-ended queue
class Deque(object):

    def __init__(self, iterable=None):
        """Initialize this queue and enqueue the given items, if any."""
        # Initialize a new linked list to store the items
        self.queue = LinkedQueue()
        if iterable is not None:
            for item in iterable:
                self.enqueue(item)

    def push_front(self, item):
        """"""
        self.queue.prepend(item)

    def push_back(self, item):
        """"""
        self.queue.enqueue(item)

    def pop_front(self):
        """"""
        if self.is_empty():
            raise ValueError('The queue is empty.')
        else:
            self.queue.dequeue()

    def pop_back(self):
        """"""
        if self.is_empty():
            raise ValueError('The queue is empty.')
        else:
            self.queue.delete(self.tail.data)
