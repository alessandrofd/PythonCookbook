__author__ = 'Alessandro.Dantas'

# To perform case-insensitive text operations, you need to use the re module and supply the re.IGNORECASE flag to
# various operations. For example:

import re

text = 'UPPER PYTHON, lower python, Mixed Python'
print(re.findall('python', text, flags=re.IGNORECASE))

new_text = re.sub('python', 'snake', text, flags=re.IGNORECASE)
print(new_text)

# The last example reveals a limitation that replacing text won't match the case of the matched text. If you need to fix
# this, you might have to use a support function as in the following:

def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

# Here is an example of using this last function:

new_text = re.sub('python', matchcase('snake'), text, flags=re.IGNORECASE)
print(new_text)

# DISCUSSION

# For simple cases, simply providing the re.IGNORECASE is enough to perform case-insensitive matching. However, be
# aware that this may not be enough for certain kinds of Unicode matching involving case folding. See Recipe 2.10 for
# more details.