#!python
from stack import Stack
from linkedlist import LinkedList
from queue import Queue


class BinaryTreeNode(object):

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # Check if either left child or right child has a value
        return self.left is not None or self.right is not None

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        left_height = 0
        right_height = 0
        # TODO: Check if left child has a value and if so calculate its height
        if self.left:
            left_height += self.left.height() + 1
        # TODO: Check if right child has a value and if so calculate its height
        if self.right:
            right_height += self.right.height() + 1
        # Return one more than the greater of the left height and right height
        return max(left_height, right_height)

        return max(self.left.height(), self.right.height()) + 1 if self is not None else 0

class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        self.vertex = dict()
        if items is not None:
            for item in items:
                self.insert(item)


    def printt(self):
        return self.vertex

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        TODO: Best and worst case running time: ??? under what conditions?"""
        # TODO: Check if root node has a value and if so calculate its height
        return self.root.height() if self.root else None

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return the node's data if found, or None
        return node.data if node else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # TODO: Create a new root node
            self.root = BinaryTreeNode(item)
            # TODO: Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        # parent = self._find_parent_node_iterative(item)
        # create a list to hold all nodes with neighbors
        # check if node is already in keys
        if parent not in self.vertex:
            self.vertex[parent] = list()
        # TODO: Check if the given item should be inserted left of parent node
        if item < parent.data:
            # TODO: Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
            # add to parent's neighbor list
            self.vertex[parent].append(parent.left)
        # TODO: Check if the given item should be inserted right of parent node
        elif item > parent.data:
            # TODO: Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
            # add to parent's neighbor list
            self.vertex[parent].insert(0, parent.right)
        # TODO: Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Descend to the node's left child
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # TODO: Check if the given item matches the node's data
        if item == node.data:
            # Return the parent of the found node
            return parent
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            return self._find_parent_node_recursive(item, node.left, node)  # Hint: Remember to update the parent parameter
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            return self._find_parent_node_recursive(item, node.right, node)  # Hint: Remember to update the parent parameter

    def _replace_with_successor_node(self, node):
        """Find the node in the right subtree of the given node that has the minimum value
            then replace node with successor node"""
        # starting node: right subtree
        succ = node.right
        succ_parent = node

        while succ.left:
            succ_parent = succ
            succ = succ.left

        node.data = succ.data
        succ_parent.left = succ.left


    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        TODO: Best case running time: ??? under what conditions?
        TODO: Worst case running time: ??? under what conditions?"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        node = self._find_node_iterative(item)
        # Case 1: item has no children nodes
        if node.left is None and node.right is None:
            # special case
            if node is self.root:
                self.root = None
                return
            # find parent of node
            parent = self._find_parent_node_recursive(node)
            if parent.left == node:
                parent.left = None
            else:
                parent.right = None
            return

        # Case 2: item has 1 child node
        if node.left is None:
            # special case
            if node is self.root:
                self.root = self.root.right
                return

            parent = self._find_parent_node_recursive(node)
            # link node's right child as node's parent child
            if parent.left == node:
                parent.left = node.right
            else:
                parent.right = node.right
            return

        # Case 3: item has 2 children nodes
        # find successor of item: 1 step right, all the way left
        if node.right.left is None:
            #  special case: the right node of node is te successor
            # repace node with node.right
            node.data = node.right.data
            node.right = node.right.right

            return

        self._replace_with_successor_node(node)


    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
            # self._traverse_in_order_iterative(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse left subtree, if it exists
        if node is not None:
            self._traverse_in_order_recursive(node.left, visit)
        # TODO: Visit this node's data with given function
            visit(node.data)
        # TODO: Traverse right subtree, if it exists
            self._traverse_in_order_recursive(node.right, visit)
        else:
            return

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: O(n+m) as n is number of nodes and m as number of edges Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)



    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            # self._traverse_pre_order_recursive(self.root, items.append)
            self._traverse_pre_order_iterative(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Visit this node's data with given function
        if node is not None:
            visit(node.data)
        # TODO: Traverse left subtree, if it exists
            self._traverse_pre_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
            self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)
        s = Stack()
        # push root node to the stack
        s.push(self.root)
        while s.length() > 0:
            # get the top node in the stack
            current = s.pop()
            # if node is a leaf, then its neighbors list is empty
            if current.is_leaf():
                self.vertex[current] = []
            for neighbor in self.vertex[current]:
                s.push(neighbor)
            visit(current.data)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            # self._traverse_post_order_recursive(self.root, items.append)
            self._traverse_post_order_iterative(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse left subtree, if it exists
        if node is not None:
            self._traverse_post_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
            self._traverse_post_order_recursive(node.right, visit)
        # TODO: Visit this node's data with given function
            visit(node)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)
        stack_1 = Stack()
        stack_2 = Stack()
        # push root node to the stack
        stack_1.push(self.root)

        while stack_1.length() > 0:
            # get the top node in the stack
            current = stack_1.pop()
            stack_2.push(current)
            # if node is a leaf, then its neighbors list is empty
            if current.is_leaf():
                self.vertex[current] = []

            for neighbor in reversed(self.vertex[current]):
                stack_1.push(neighbor)


        while stack_2.length() > 0:
            visit(stack_2.pop().data)



    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Create queue to store nodes not yet traversed in level-order
        queue = Queue()
        # TODO: Enqueue given starting node
        queue.enqueue(start_node)
        # TODO: Loop until queue is empty
        while queue.length() > 0:
            # TODO: Dequeue node at front of queue
            node = queue.dequeue()
            # TODO: Visit this node's data with given function
            visit(node.data)
            # TODO: Enqueue this node's left child, if it exists
            if node.left:
                queue.enqueue(node.left)
            # TODO: Enqueue this node's right child, if it exists
            if node.right:
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    # items = [4, 2, 6, 1, 3, 5, 7]
    items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()

    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))



    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nDeleting  items:')
    tree.delete(12)
    # print('delete({}): {}'.format(8))



    print('\nTraversing items:')
    # print('items in-order:    {}'.format(tree.items_in_order()))
    # print('items pre-order:   {}'.format(tree.items_pre_order()))
    # print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))
    # print(tree.printt())


if __name__ == '__main__':
    test_binary_search_tree()
