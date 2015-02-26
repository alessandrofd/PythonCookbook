__author__ = 'Alessandro.Dantas'

"""
Consider two dictionaries:
"""

a = {
    'x': 1,
    'y': 2,
    'z': 3
}

b = {
    'w': 10,
    'x': 11,
    'y': 2
}

"""
To find out what the two dictionaries have in commonn, simply perform common set operations using the keys() or items()
methods. For example:
"""

# Find keys in common
print(a.keys() & b.keys())  # {'x', 'y' }

# Find keys in a that are not in b
print(a.keys() - b.keys())  # {'z'}

# Find (key, value) pairs in common
print(a.items() & b.items())  # { ('y', 2) }

"""
These kinds of operations can also be used to alter or filter dictionary contents. For example, suppose you want to
make a new dictionary with selected keys removed. Here is some sample code using a dictionary comprehension:
"""

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z', 'w'}}
print(c)  # c is ['x': 1, 'y': 2}

"""
DISCUSSION

A dictionary is a mapping between a set of keys and values. The keys() method of a dictionary returns a keys-view object
that exposes the keys. A little-known feature of keys views is that they also support common set operations such as
unions, intersections, and differences. Thus, if you need to perform common set operations with dictionary keys, you can
often just use the keys-view objects directly without first converting them into a set.

The items() method of a dictionary returns an items-view object consisting of (key, value) pairs. This object supports
similar set operations and can be used to perform operations such as finding ou which key-value pairs two dictionaries
have in common.

Although similar, the values() method of a dictionary does not support the set operations described in this recipe. In
part, this is due to the fact that unlike keys, the items contained in values view aren't guaranteed to be unique. This
alone makes certain set operations of questionable utility. However, if you must perform such calculations, they can be
accomplished by simply converting the values to a set first.
"""

