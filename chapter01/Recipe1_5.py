__author__ = 'Alessandro.Dantas'

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)

q = PriorityQueue()
q.push(Item('foo'), 1)
q.push(Item('bar'), 5)
q.push(Item('spam'), 4)
q.push(Item('grok'), 1)

print(q.pop())
print(q.pop())
print(q.pop())
print(q.pop())

"""
Observe how the first pop() operation returned the item with the highest priority. Also observe how the two items with
the same priority (foo and grok) were returned in the same order in which they where inserted into the queue.
"""

"""
The core of this recipe concerns the use of the heapq module. The functions heapq.heappush() and heapq.heappop() insert
and remove items from a list _queue in a way such that the first item in the list has the smallest priority (as discussed
in Recipe 1.4). The heappop() method always returns the "smallest" item, so that is the key to making the queue pop the
correct items. Moreover, since the push and pop operations have O(log N) complexity where N is the number of items in the
heap, they are fairly efficient even for fairly large values of N.

In this recipe, the queue consists of tuples of the form (-priority, index, item). The priority value is negated to get
the queue to sort items from highest priority to lowest priority. This is opposite of the normal heap ordering, which
sorts from lowest to highest value.

The role of the index variable is to properly order items with the same priority level. By keeping a constantly
increasing index, the items will be sorted according to the order in which they were inserted. However, the index also
serves an important role in making the comparison operations work for items that have the same priority level.

To elaborate on that, instances of Item in the example can't be ordered. For example:

a = Item('foo')
b = Item('bar')
a < b
TypeError: unorderable types: Item() < Item()

By introducing the extra index and making (priority, index, item) tuples, you avoid this problem entirely since no two
 tuples will ever have the same value for index (and Python never bothers to compare the remaining tuple values once the
 result of comparison can be determined):
"""

a = (1, 0, Item('foo'))
b = (5, 1, Item('bar'))
c = (1, 2, Item('grok'))
print(a < b)
print(a < c)

"""
If you want to use this queue for communication between threads, you need to add appropriate locking and signaling. See
Recipe 12.3 for an example on how to do this.

The documentation for the heapq module has further examples and discussion concerning the theory and implementation of
heaps.
"""

