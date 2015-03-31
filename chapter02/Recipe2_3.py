__author__ = 'Alessandro'

# The fnmatch module provides two functions - fnmatch() and fnmatchcase() - that can be used to
# perform such matching. The usage is simple:

from fnmatch import fnmatch, fnmatchcase
print(fnmatch('foo.txt', '*.txt'))
print(fnmatch('foo.txt', '?oo.txt'))
print(fnmatch('Dat45.csv', 'Dat[0-9]*'))
names = ['Dat1.csv', 'Dat2.csv', 'config.ini', 'foo.py']
print([name for name in names if fnmatch(name, 'Dat*.csv')])

# Normally, fnmatch() matches patterns using the same case-sensitive rules as the system's
# underlying filesystem (which varies based on operating system). For example:

# On OS X (Mac)
#print(fnmatch('foo.txt', '*.TXT'))  # Outputs: False

# On Windows
print(fnmatch('foo.txt', '*.TXT'))  # Outputs: True

# If this distinction matters, use fnmatchcase() instead. It matches exactly based on the lower- and
# uppercase conventions that you supply:

print(fnmatchcase('foo.txt', '*.TXT'))

# An often overlooked feature of these functions is their potential use with data processing of
# nonfilename strings. For example, suppose you have a list of street addresses like this:

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY'
]

# You could write list comprehensions like this:

from fnmatch import fnmatch
print([addr for addr in addresses if fnmatchcase(addr, '* ST')])
print([addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9] *CLARK*')])

# DISCUSSION

# The matching performed by fnmatch sits somewhere between the functionality of simple string
# methods and the full power of regular expressions. If you're just trying to provide a simple
# mechanism for allowing wildcards in data processing operations, it's often a reasonable solution.
# If you're actually trying to write code that matches filenames, use the glob module instead. See
# Recipe 5.13.