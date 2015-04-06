__author__ = 'Alessandro'

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Example
root = Node(0)
child1 = Node(1)
child2 = Node(2)
root.add_child(child1)
root.add_child(child2)
for ch in root:
    print(ch)
# Outputs Node(1), Node(2)

# In this code, the __iter__() method simply forwards the iteration request to the internally held _children attribute.

# DISCUSSION
#
# Python's iterator protocol requires __iter__() to return a special iterator object that implements a __next__() method
# to carry out the actual iteration. If all you are doing is iterating over the contents of another container, you really
# don't have to worry about the underlying details of how it works. All you need to do is to forward the iteration
# request along.


# The use of iter() function here is a bit of a shortcut that cleans up the code. iter(s) simply returns the underlying
# iterator by calling s.__iter__(), much in the same way that len(s) invokes s.__len__().