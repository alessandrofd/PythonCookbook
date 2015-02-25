__author__ = 'Alessandro.Dantas'

p = (4, 5)
x, y = p
print(x)
print(y)

data = ['ACME', 50, 91.1, (2012, 12, 21)]
name, shares, price, date = data
print(name, date)

name, shares, price, (year, mon, day) = data
print(name, year, mon, day)

# If there is a mismatch in the number of elements, you'll get an error.
"""
p = (4, 5)
x, y, z = p
"""

# Unpacking actually works with any objects that happens to be iterable, not just tuples or lists. This includes strings,
# files, iterators, and generators.

s = 'Hello'
a, b, c, d, e = s
print(a, b, e)

# When unpacking, you may sometimes want to discard certain values. Python has no special syntax for this, but you can
# often just pick a throwaway variable name for it.

data = ['ACME', 50, 91.1, (2012, 12, 21)]
_, shares, price, _ = data
print(shares, price)