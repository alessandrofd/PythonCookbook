__author__ = 'Alessandro'

s = 'pýtĥöñ\fis\tawesome\r\n'
print(s)

# The first step is to clean up the whitespace. To do this, make a small translation table and use translate():

remap = {
    ord('\t'): ' ',
    ord('\f'): ' ',
    ord('\r'): None  # Deleted
}
a = s.translate(remap)
print(a)

# As you can see here, whitespace characters such as \t and \f have been remapped to a single space. The carriage return
# \r has been deleted entirely.

# You can take this remapping idea a step further and build much bigger tables. For example, let's remove all combining
# characters:

import unicodedata
import sys
cmb_chrs = dict.fromkeys(c for c in range(sys.maxunicode) if unicodedata.combining(chr(c)))
b = unicodedata.normalize('NFD', a)
print(b)
print(b.translate(cmb_chrs))

# In this last example, a dictionary mapping every Unicode combining character to None is created using the dict.from-
# keys().

# The original input is then normalized into a decomposed form using unicodedata.normalize(). From there, the translate
# function is used to delete all of the accents. Similar techniques can be used to remove other kinds of characters
# (e.g., control characters, etc.)

# As another example, here is a translation table that maps all Unicode decimal digit characters to their equivalent in
# ASCII:

digitmap = {c: ord('0') + unicodedata.digit(chr(c))
             for c in range(sys.maxunicode)
             if unicodedata.category(chr(c)) == 'Nd'}
print(len(digitmap))

# Arabic digits
x = '\u0661\u0662\u0663'
print(x.translate(digitmap))


# Yet another technique for cleaning up text involves I/O decoding and encoding functions. The idea here is to first do
# some preliminary cleanup of the text, and then run it through a combination of encode() or decode() operations to
# strip or alter it. For example:

print(a)
b = unicodedata.normalize('NFD', a)
print(b.encode('ascii', 'ignore').decode('ascii'))

# Here the normalization process decomposed the original text into characters along with separate combining characters.
# The subsequent ASCII encoding/decoding simply discarded all of those characters in one fell swoop. Naturally, this
# would only work if getting an ASCII representation was the final goal.

# DISCUSSION

# A major issue with sanitizing text can be runtime performance. As a general rule, the simpler it is, the faster it
# will run. For simple replacements, the str.replace() method is often the fastest approach—even if you have to call it
# multiple times. For instance, to clean up whitespace, you could use code like this:

def clean_spaces(s):
    s = s.replace('\r', '')
    s = s.replace('\t', '')
    s = s.replace('\f', '')
    return s

# If you try it, you'll find that it's quite a bit faster than using translate() or an approach using a regular expres-
# sion.

# On the other hand, the translate() method is very fast if you need to perform any kind of non-trivial character-to-
# character remapping or deletion.

# In the big picture, performance is something you will have to study further in your particular application. Unfortuna-
# tely, it's impossible to suggest one specific technique that works best for all cases, so try different approaches and
# measure it.

# Although the focus of this recipe has been text, similar techniques can be applied to bytes, including simple replace-
# ments, translation, and regular expressions.
