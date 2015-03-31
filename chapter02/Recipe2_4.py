__author__ = 'Alessandro'

# If the text you're trying to match is a simple literal, you can often just use the basic string
# methods, such as str.find(), str.endswith(), str.startswith(), or similar.

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print(text == 'yeah')

# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))

# Search for the location of the first occurrence
print(text.find('no'))

# For more complicated matching, use regular expressions and the re module. To illustrate the basic
# mechanics of using regular expressions, suppose you want to match dates specified as digits, such
# as "11/27/2012". Here is a sample of how you would do it.

text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re

# Simple matching: \d+ means match one or more digits
if re.match(r'\d+/\d+/\d+', text1):
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2):
    print('yes')
else:
    print('no')

# If you're going to perform a lot of matches using the same pattern, it usually pays to precompile the regular
# expression pattern into a pattern object first. For example:

datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print('yes')
else:
    print('no')

if datepat.match(text2):
    print('yes')
else:
    print('no')

# match() always tries to find the match at the start of a string. If you want search text for all occurrences of a
# pattern, use the findall() method instead. For example:

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
print(datepat.findall(text))

# When defining regular expressions, it is common to introduce capture groups by enclosing parts of the pattern in
# parentheses. For example:

datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# Capture groups often simplify subsequent processing of the matched text because the contents of each group can be
# extracted individually. For example:

m = datepat.match('11/27/2012')
print(m)

# Extract the contents of each group
print(m.group(0))
print(m.group(1))
print(m.group(2))
print(m.group(3))
print(m.groups())
month, day, year = m.groups()

# Find all matches (notice splitting into tuples)
print(text)
print(datepat.findall(text))
for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day))

# The findall() method searches the text and finds all matches, returning them as a list. If you want to find matches
# iteratively, use the finditer() method instead. For example:

for m in datepat.finditer(text):
    print(m.groups())

# DISCUSSION

# A basic tutorial on the theory of regular expressions is beyond the scope of this book. However, this recipe
# illustrates the absolute basics of using the re module to match and search for text. The essential functionality is
# first compiling a pattern using re.compile() and then using methods such as match(), findall(), or finditer().

# When specifying patterns, it is relatively common to use raw strings such as r'(\d+)/(\d+)/(\d+)'. Such strings leave
# the backslash character uninterpreted, which can be useful in the context of regular expressions. Otherwise, you need
# to use double backslashes such as '(\\d+)/(\\d+)/(\\d+)'.

# Be aware that the match() method only checks the beginning of a string. It's possible that it will match things you
# aren't expecting. For example:

m = datepat.match('11/27/2012abdcef')
print(m)
print(m.group())

# If you want an exact, make sure the pattern includes the end-marker ($), as in the following:

datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
print(datepat.match('11/27/2012abcdef'))
print(datepat.match('11/27/2012'))

# Last, if you're just doing simple text matching/searching operation, you can often skip the compilation step and use
# module-level functions in the re module instead. For example:

print(re.findall(r'(\d+)/(\d+)/(\d+)', text))

# Be aware, though, that if you're going to perform a lot of matching or searching, it usually pays to compile the
# pattern first and use it over and over again. The module-level functions keep a cache of recently compiled patterns,
# so there isn't a huge performance hit, byt you'll save a few lookups and extra processing by using your own compiled
# pattern.
