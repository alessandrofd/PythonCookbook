__author__ = 'Alessandro'

d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

"""
The choice of whether or not to use lists or sets depends on intended use. Use a list if you want to
preserve the insertion order of the items. Use a set if you want to eliminate duplicates (and don't
care about the order.

To easily construct such dictionaries, you can use defaultdict in the collections module. A feature
of defaultdict is that it automatically initializes the first value so you can simply focus on
adding items.
"""

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['a'].append(4)
print(d)

d = defaultdict(set)
d['a'].add(1)
d['a'].add(2)
d['a'].add(4)
print(d)

"""
One caution with defaultdic is that it will automatically create dictionary entries for keys
accessed later on (even if they aren't currently found in the dictionary). If you don't want this
behavior, you might use setdefault() on an ordinary dictionary instead. For example:
"""

d = {} # A regular dictionary
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

"""
However, man programmers find setdefault() to be a little unnatural - not to mention the fact that it
always creates a new instance of the initial value on each invocation (the empty list [] in the
example).
"""

"""
In principle, constructing a multivalued dictionary is simple. However, initialization of the first
value can be messy if you try to do it yourself. For, example, you might have code that looks like
this:
"""

pairs = [
    ('a', 1),
    ('a', 2),
    ('b', 4),
]
d = {}
for key, value in pairs:
    if key not in d:
        d[key] = []
    d[key].append(value)
print(d)

"""
Using a defaultdict simply leads to much cleaner code:
"""

d = defaultdict(list)
for key, value in pairs:
    d[key].append(value)
print(d)

"""
This recipe is strongly related to the problem of grouping records together in data processing problems.
See Recipe 1.15 for an example.
"""