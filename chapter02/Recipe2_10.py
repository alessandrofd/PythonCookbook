__author__ = 'Alessandro'

# By default, the re module is already programmed with rudimentary knowledge of certain Unicode character classes. For
# example, \d already matches any Unicode digit character:

import re
num = re.compile('\d+')

# ASCII digits
print(num.match('123'))

# Arabic digits
print(num.match('\u0661\u0662\u0663'))

# If you need to include specific Unicode characters in patterns, you can use the usual escape sequence for Unicode
# characters (e.g., \uFFFF or \uFFFFFFFF). For example, here is a regex that matches all characters in a few different
# Arabic code pages:

arabic = re.compile('[\u0600-\u06ff\u0750-\u077f\u08a0-\u08ff]+')

# When performing matching and searching operations, it's a good idea to normalize and possibly sanitize all text to a
# standard form first (see Recipe 2.9). However, it's also important to be aware of special cases. For example, consider
# the behavior of case-insensitive matching combined with case folding:

pat = re.compile('stra\u00dfe', re.IGNORECASE)
s = 'straße'
print(pat.match(s))          # Matches
print(pat.match(s.upper()))  # Doesn't match
print(s.upper())             # Case folds

# DISCUSSION

# Mixing Unicode and regular expressions is often a good way to make your head explode. If you're going to do it
# seriously, you should consider installing the third-party regex library (https://pypi.python.org/pypi/regex), which
# provides full support for Unicode case folding, as well as a variety of other interesting features, including
# approximate matching.