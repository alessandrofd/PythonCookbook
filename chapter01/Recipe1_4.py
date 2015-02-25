__author__ = 'Alessandro.Dantas'

import heapq

nums = [ 1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # Prints [42, 37, 23]
print(heapq.nsmallest(3, nums)) # Prints [-4, 1, 2]

"""
Both functions also accept a key parameter that allows them to be used with more complicated data structures.
"""

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
print(cheap)
expensive = heapq.nlargest(3, portfolio, key=lambda s: s['price'])
print(expensive)

"""
If you are looking for the N smallest or largest items and N is small compared to the overall size of the collection,
these functions provide superior performance. Underneath the covers, they work by first converting the data into a list
where items are ordered as a heap. For, example:
"""

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heap = list(nums)
heapq.heapify(heap)
print(heap)

"""
The most important feature of a heap is that heap[0] is always the smallest item. Moreover, subsequent items can be
easily found using the heapq.heappop() method, which pops off the first item and replaces it with the next smallest
item (an operation that requires O(log N)operations where N is the size of the heap). For example, to find the three
smallest items, you would do this:
"""
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))

"""
The nlargest() and nsmallest() functions are most appropriate if you are trying to find a relatively small number of
items. If you are simply trying to find the single smallest or largest item (N=1), it is faster to use min() and max().
Similarly, if N is about the same size as the collection itself, it is usually faster to sort it first and take a slice
(i.e., use sorted(items)[:N] or sorted(items)[-N:]). It should be noted that the actual implementation of nlargest() and
nsmallest() is adaptive in how it operates and will carry out some of these optimizations on your behalf (e.g., using
sorting if N is close to the same size as the input).

Although it's not necessary to use this recipe, the implementation of a heap is an interesting and worthwhile subject of
study. This can usually be found in any decent book on algorithms and data structures. The documentation for the heapq
module also discusses the underlying implementation details.
"""