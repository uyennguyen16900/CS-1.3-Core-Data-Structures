# from linkedlist import LinkedList

class Node(object):
    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None
        self.previous = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)

class DoublyLinkedList(object):
    def __init__(self, iterable=None):
        """Initialize this doubly linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list of all items in this linked list.
        Best and worst case running time: Theta(n) for n items in the list
        because we always need to loop through all n nodes."""
        # Create an empty list of results
        result = []  # Constant time to create a new list
        # Start at the head node
        node = self.head  # Constant time to assign a variable reference
        # node.previous = None
        # Loop until the node is None, which is one node too far past the tail
        while node is not None:  # Always n iterations because no early exit
            # Append this node's data to the results list
            result.append(node.data)  # Constant time to append to a list
            # Skip to the next node
            node = node.next  # Constant time to reassign a variable
        # Now result contains the data from all nodes
        return result  # Constant time to return a list

    def is_empty(self):
        """Return True if this linked list is empty, or False."""
        return self.head is None

    def append(self, item):
        """Insert the given item at the head of this doubly linked list"""
        # Create a new node to hold the given item
        new_node = Node(item)
        new_node.previous = self.tail

        # Check if the node is empty
        if self.is_empty():
            self.head = new_node
        else:
            self.tail.next = new_node
        # Update new node to tail
        self.tail = new_node
        self.size += 1

    def prepend(self, item):
        """"""
        new_node = Node(item)
        new_node.next = self.head
        new_node.previous = None
        if self.is_empty():
            self.tail = new_node
        else:
            self.head.previous = new_node
        self.head = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this doubly linked list satisfying the given quality"""
        node = self.head
        pass


    def delete(self, item):
        """"""
        current_node = self.head.next
        found = False
        return current_node
        while not found and current_node is not None:
            if current_node.data == item:
                found = True
                # current_node.previous.next = current_node.next
            else:
                current_node = current_node.next

        if found:
            if current_node is not self.head and current_node is not self.tail:
                current_node.previous.next = current_node.next
                # unlink the found node from its next node
                current_node.next = None

            if current_node is self.head:
                self.head = current_node.next
                current_node.next = None

            if current_node is self.tail:
                # check if the previous node before tail is not none
                if self.tail.previous is not None:
                    self.tail.previous.next = None

                self.tail = self.tail.previous

            self.size -= 1

        else:
            raise ValueError('Item not found: {}'.format(item))

    def printList(self, node):
        """Prints content of linked list starting from the given node"""
        print( "\nTraversal in forward direction:")
        while(node is not None):
            print( " % d" %(node.data))
            last = node
            node = node.next

        print( "\nTraversal in reverse direction:")
        while(last is not None):
            print( " % d" %(last.data))
            last = last.previous

def test_linked_list():
    ll = DoublyLinkedlist()
    print(ll)

    print('Appending items:')
    ll.append('A')
    print(ll)
    ll.append('B')
    print(ll)
    ll.append('C')
    print(ll)
    ll.prepend('D')
    print(ll)
    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('size: {}'.format(ll.size))

    print('Deleting items:')
    print(ll.delete('B'))
    # print(ll)
    # ll.delete('C')
    # print(ll)
    # ll.delete('A')
    # print(ll)
    # print('head: {}'.format(ll.head))
    # print('tail: {}'.format(ll.tail))
    # print('size: {}'.format(ll.size))



if __name__ == '__main__':
    # test_linked_list()
    llist = DoublyLinkedList()

    # Insert 6. So the list becomes 6->None
    llist.append(6)

    # Insert 7 at the beginning.
    # So linked list becomes 7->6->None
    llist.prepend(7)

    # Insert 1 at the beginning.
    # So linked list becomes 1->7->6->None
    llist.prepend(1)

    # Insert 4 at the end.
    # So linked list becomes 1->7->6->4->None
    llist.append(4)

    llist.printList(llist.head)
