# Recipe 4.14. Flattening a Nested Sequence
#
# Problem: You have a nested sequence that you want to flatten into a single list of values.
#
# Solution: This is easily solved by writing a recursive generator function involving a "yield from" statement. For
#   example:

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x

items = [1, 2, [3, 4, [5, 6], 7], 8]

for x in flatten(items):
    print(x)

# In the code, the isinstance(x, Iterable) simply checks to see if an item is iterable. If so, "yield from" is used to
# emit all of its values as a kind of subroutine. The end result is a single sequence of output with no nesting.
#
# The extra argument ignore_types and the check for "not isisntance(x, ignore_types)" is there to prevent strings and
# bytes from being interpreted as iterables and expanded as individual characters. This allows nested lists of strings
# to work in the way that most people would expect. For example:

print('\n### Strings not treated as Iterable ###\n')

items = ['Dave', 'Paula', ['Thomas', 'Lewis']]
for x in flatten(items):
    print(x)

# DISCUSSION
#
# The "yield from" statement is a nice shortcut to use if you ever want to write generators that call other generators
# as subroutines. If you don't use it, you need to write code that uses an extra "for" loop. For example:

def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            for i in flatten(x):
                yield i
            else:
                yield x

# Although it's only a minor change, the "yield from" statement just feels better and leads to cleaner code.
#
# As noted, the extra check for strings and bytes is there to prevent the expansion of those types into individual
# characters. If there are other types that you don't want expanded, you can supply a different value for the "ignore_
# types" argument.
#
# Finally, it should be noted that "yield from" has a more important role in advanced programs involving coroutines and
# generator-based concurrency. See Recipe 12.12 for another example.
