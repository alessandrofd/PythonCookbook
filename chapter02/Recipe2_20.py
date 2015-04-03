__author__ = 'Alessandro'

data = b'Hello World'
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# Such operations also work with byte arrays. For example:

print('\n### Byte Arrays ###\n')

data = bytearray(b'Hello World')
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello', b'Hello Cruel'))

# You can apply regular expression pattern matching to byte strings, byt the patterns themselves need to be specified as
# bytes. For example:

print('\n### Regular Expressions ###\n')

data = b'FOO:BAR,SPAM'
import re
#re.split('[:,]', data) # TypeError: can't use a string pattern on a bytes-like object
print(re.split(b'[:,]', data))  # Notice: patterns as bytes

# DISCUSSION

# For the most part almost all of the operations available on text strings will work on byte strings. However, there are
# a few notable differences to be aware of. First, indexing of byte strings produces integers, not individual characters.
# For example:

print('\n### Indexing of Byte Strings ###\n')

a = 'Hello World'  # Text string
print(a[0])
print(a[1])

b = b'Hello World'  # Byte string
print(b[0])
print(b[1])

# The difference in semantics can affect programs that try to process byte-oriented data on a character-by-character
# basis.

# Second, byte strings don't provide a nice string representation and don't print cleanly unless first decoded into a
# text string. For example:

print('\n### Printing Byte Strings ###\n')

s = b'Hello World'
print(s)
print(s.decode('ascii'))

# Similarly, there aer no string formatting operations available to byte strings.

# b'%10s %10d %10.2f' % (b'ACME', 100, 490.1)  # TypeError: unsupported operand type(s) for %: 'bytes' and 'tuple'
# b'{} {} {}'.format(b'ACME', 100, 490.1)  # AttributeError: 'bytes' object has no attribute 'format'

# If you want to do any kind of formatting applied to byte strings, it should be done using normal text strings and
# encoding. For example:

print('{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii'))

# Finally, you need to be aware that using a byte string can change the semantics of certain operations—specially those
# related to the filesystem. For example, if you supply a filename encoded as bytes instead of a text string, it usually
# disables filename encoding/decoding. For example:

print('\n### Byte Stings in file operations ###\n')

# Write a UTF-8 filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# Get a directory listing
import os
print(os.listdir('.'))   # Text string (names as decoded)
print(os.listdir(b'.'))  # Byte string (names left as bytes)

# Notice in the last part of this example how giving a byte string as the directory name caused the resulting filenames
# to be returned as uncoded bytes. The filename shown in the directory listing contains raw UTF-8 encoding. See Recipe
# 5.15 for some related issues concerning filenames.

# As a final comment, some programmers might be inclined to use byte strings as an alternative to text strings due to a
# possible performance improvement. Although it's true that manipulating bytes tends to be slightly more efficient than
# text (due to the inherent overhead related to Unicode), doing so usually leads to very messy and nonidiomatic code.
# You'll ofter find that byte strings don't play well with a lot of other parts of Python, and that you end up having to
# perform all sorts of manual encoding/decoding operations yourself to get things to work right. Frankly, if you're
# working with text, use normal text strings in your program, not byte stings.