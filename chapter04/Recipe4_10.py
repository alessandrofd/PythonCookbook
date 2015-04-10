# Recipe 4.10. Iterating Over the Index-Value Pairs of a Sequence
#
# Problem: You want to iterate over a sequence, but would like to keep track of which element of the sequence is
#   currently being processed.
#
# Solution: The built-in enumerate() functions handles this quite nicely:

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list):
    print(idx, val)

# For printing output with canonical line numbers (where you typically start the numbering at 1 instead of 0), you can
# pass in a start argument:

print('\n### With start argument ###\n')

my_list = ['a', 'b', 'c']
for idx, val in enumerate(my_list, 1):
    print(idx, val)

# This case is especially useful for tracking line numbers in files should you want a line number in an error message:
#
# def parse_data(filename):
#     with open(filename, 'rt') as f:
#         for lineno, line in enumerate(f, 1):
#             fields = line.split()
#             try:
#                 count = int(fields[1])
#                 ...
#             except ValueError as e:
#                 print('Line {}: Parse error: {}'.format(lineno, e))

# enumerate() can be handy for keeping track of the offset into a list for occurrences of certain values, for example.
# So, if you want to map words in a file to the lines in which they occur, it can easily be accomplished using
# enumerate() to map each word to the line offset in the file where it was found:

from collections import defaultdict
word_summary = defaultdict(list)

with open('myfile.txt', 'r') as f:
    lines = f.readlines()

for idx, line in enumerate(lines):
    # Create a list of words in current line
    words = [w.strip().lower() for w in line.split()]
    for word in words:
        word_summary[word].append(idx)

# If you print word_summary after processing the file, it'll be a dictionary (a defaultdict to be precise), and it'll
# have a key for each word. The value for each word-key will be a list of line numbers that word occurred on. If the
# word occurred twice in a single line, that line number will be listed twice, making it possible to identify various
# simple metrics about the text.

# DISCUSSION
#
# enumerate() is a nice shortcut for situations where you might also be inclined to keep your own counter variable. You
# could write code like this:

lineno = 1
for line in f:
    # Process line
    ...
    lineno +=1

# But it's usually much more elegant ( and less error prone) to use the enumerate() instead:

for lineno, line in enumerate(f):
    # Process line
    ...

# The value returned by enumerate() is an instance of an enumerate object, which is an iterator that returns successive
# tuples consisting of a counter and the value returned by calling next() on the sequence you've passed in.
#
# Although a minor point, it's worth mentioning that sometimes it is easy to get tripped up when applying enumerate() to
# a sequence of tuples that are also being unpacked.

data = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Correct!
for n, (x, y) in enumerate(data):
    ...

# Error
for n, x, y in enumerate(data):
    ...