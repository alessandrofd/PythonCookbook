__author__ = 'Alessandro.Dantas'

"""
The following code performs a simple text match on a sequence of lines and yields the matching line along the previous
N lines of context when found.
"""

from collections import deque

def search(lines, pattern, history=5):
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_lines
        previous_lines.append(line)

with open('somefile.txt') as f:
    for line, prevlines in search(f, 'python', 5):
        for pline in prevlines:
            print(pline, end='')
        print(line, end='')
        print('-'*20)

"""
When writing code to search for items, it is common to use a generator function involving yield, as show in this
recipe's solution. This decouples the process of searching from the code that uses the results. If you're new to
 generators, see Recipe 4.3.
"""


"""
Using deque(maxlen=N) creates a fixed-sized queue. When new items are added and the queue is full, the oldest item is
automatically removed.
"""
q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)

q.append(4)
print(q)

q.append(5)
print(q)

"""
Although you could manually perform such operations on a list (e.g., appending, deleting, etc.), the queue solution is
far more elegant and runs a lot faster.

More generally, a deque can be uses whenever you need a simple queue structure. If you don't give it a maximum size, you
get an unbounded queue that lets you append and pop items on either end.
"""

print ('-' * 20)
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.appendleft(4)
print(q)
print(q.pop())
print(q)
print(q.popleft())
print(q)
