# Recipe 4.8. Skipping the First Part of as Iterable
#
# Problem: You want to iterate over items in an iterable, but the first few items aren't of interest and you just want
#   to discard them.
#
# Solution: The iterttools module has a few functions that can be used to address this task. The first is the
#   itertools.dropwhile() function. To use it, you supply a function and an iterable. The returned iterator discards the
#   first items in the sequence as long as the supplied function returns True. Afterward, the entirety of the sequence
#   is produced.
#
# To illustrate, suppose you are reading a file that starts with a series of comment lines. For example:

with open('passwd.txt') as f:
    for line in f:
        print(line, end='')

# If you want to skip all of the initial comment lines, here's one way to do it:

print('\n### With dropwhile ###\n')

from itertools import dropwhile
with open('passwd.txt') as f:
    for line in dropwhile(lambda line: line.startswith('#'), f):
        print(line, end='')

# This example is based of skipping the first items according to a test function. If you happen to know the exact number
# of items you want to skip, then you can use itertools.islice() instead. For example:

print('\n### With islice ###\n')

from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items, 3, None):
    print(x)

# In this example, the last None argument to islice() is required to indicate that you want everything beyond the first
# three items as opposed to only the first three items (e.g., a slice of [3:] as opposed to a slice of [:3]).
#
# DISCUSSION
#
# The dropwhile() and islice() functions are mainly convenience functions that you can use to avoid writing rather messy
# code such as this:

print('\n### Messy way to do it ###\n')

with open('passwd.txt') as f:
    # Skip over the initial comments
    while True:
        line = next(f, '')
        if not line.startswith('#'):
            break

    # Process remaining lines
    while line:
        # Replace with useful processing
        print(line, end='')
        line = next(f, None)


# Discarding the first part of an iterable is also slightly different from simply filtering all of it. For example, the
# first part of this recipe might be rewritten as follows:

print('\n### Simply filtering ###\n')

with open('passwd.txt') as f:
    lines = (line for line in f if not line.startswith('#'))
    for line in lines:
        print(line, end='')

# This will discard the comment lines at the start, but will also discard all such lines throughout the entire file. On
# the other hand, the solution only discards items until an item no longer satisfies the supplied test. After that, all
# subsequent items are returned without filtering.
#
# Last, but not least, it should be emphasized that this recipe works with all iterables, including those whose size
# can't be determined in advance. This includes generators, files, and similar kinds of objects.