# Recipe 4.9. Iterating Over All Possible Combinations or Permutations
#
# Problem: You want to iterate over all of the possible combinations or permutations of a collection of items.
#
# Solution: The itertools module provides three functions for this task. The first of these—itertools.permutations()—
#   takes a collection of items and produces a sequence of tuples that rearranges all of the items into all possible
#   permutations (i.e., it shuffles them into all possible configurations). For example:

items = ['a', 'b', 'c']
from itertools import permutations
for p in permutations(items):
    print(p)

# If you want all permutations of a smaller length, you can give an optional length argument. For example:

print('\n### With length argument ###\n')

for p in permutations(items, 2):
    print(p)

# Use itertools.combinations() to product a sequence of combinations of items taken from the input. For example:

print('\n### Combinations ###\n')

from itertools import combinations
for c in combinations(items, 3):
    print(c)

for c in combinations(items, 2):
    print(c)

for c in combinations(items, 1):
    print(c)

# For combinations(), the actual order of the elements is not considered. That is, the combination ('a', 'b') is consi-
# dered to be the same as ('b', 'a') (which is not produced);
#
# When producing combinations, chosen items are removed from the collection of possible candidates (i.e., if 'a' has
# already been chosen, then it is removed from consideration). The itertools.combinations_with_replacement() function
# relaxes this, and allows the same item to be chosen more than once. For example:

print('\n### Combinations with replacement ###\n')

from itertools import combinations_with_replacement
for c in combinations_with_replacement(items, 3):
    print(c)

# DISCUSSION
#
# This recipe demonstrates only some of the power found in the itertools module. Although you could certainly write code
# to produce permutations and combinations yourself, doing so would probably require more that a fair bit of thought.
# When faced with seemingly complicated iteration problems, it always pays to look at itertools first. If the problem is
# common, chances are a solution is already available.

