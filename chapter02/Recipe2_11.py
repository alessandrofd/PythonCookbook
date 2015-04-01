__author__ = 'Alessandro'

# The strip() method can be used to strip characters from the beginning or end of a string. lstrip() and rstrip()
# perform stripping from the left or right side, respectively. By default, these methods strip whitespace, but other
# characters can be given.

# Whitespace stripping
s = '       hello world    \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# Character stripping
t = '---------hello=========='
print(t.lstrip('-'))
print(t.strip('-='))

# DISCUSSION

# The various strip() methods are commonly used when reading and cleaning up data for later processing. For example, you
# can use them to get rid of whitespace, remove quotations, and other tasks.

# Be aware that stripping does not apply to any text in the middle of the string. For example:

s = '    hello      world  \n'
s = s.strip()
print(s)

# If you needed to do something to the inner space, you would need to use another technique, such as using the replace()
# method or a regular expression substitution. For example:

print(s.replace(' ', ''))

import re
print(re.sub('\s+', ' ', s))

# It is often the case that you want to combine string stripping operations with some other kind of iterative processing
# such as reading lines of data from a file. If so, this is one area where a generator expression can be useful. For
# example:

# with open(filename) as f:
#     lines = (line.strip() for line in f)
#     for line in lines;
#     ...

# Here, the expression lines = (line.strip() for line in f) acts as a kind of data transform. It's efficient because it
# doesn't read the data into any kind fo temporary list first. It just creates an iterator where all of the lines
# produced have the stripping operation applied to them.

# For even more advanced stripping, you might want to turn to the translate() method. See the next recipe on sanitizing
# strings for further details.