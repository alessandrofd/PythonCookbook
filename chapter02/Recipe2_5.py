__author__ = 'Alessandro.Dantas'

# For simple literal patterns, use the str.replace() method. For example:

text = 'yeah, but no, but yeah, but no, but yeah'
print(text.replace('yeah', 'yep'))

# For more complicated patterns, use the sub() functions/methods in the re module. To illustrate, suppose you want to
# rewrite dates from "11/27/2012" as "2012-11-27." Here is a sample of how to do it:

text = 'Today in 11/27/2012. PyCon starts 3/13/2013'
import re
new_text = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(new_text)

# The first argument to sub() is the pattern to match and the second argument is the replacement pattern. Backslashed
# digits such as \3 refer to capture group numbers in the pattern.

# If you're going to perform repeated substitutions of the same pattern, consider compiling it first for better
# performance. For example:

import re
date_pattern = re.compile(r'(\d+)/(\d+)/(\d+)')
new_text = date_pattern.sub(r'\3-\1-\2', text)
print(new_text)

# For more complicated substitutions, it's possible to specify a substitution callback function instead. For example:

from calendar import month_abbr


def change_date(m):
    month_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), month_name, m.group(3))

new_text = date_pattern.sub(change_date, text)

# As input, the argument to the substitution callback is a match object, as returned by match() or find(). Use the
# .group() method to extract specific parts of the match. The function should return the replacement text.

# If you want to know how many substitutions were made in addition to getting the replacement text, use re.subn()
# instead. For example:

new_text, n = date_pattern.subn(r'\3-\1-\2', text)
print(new_text)
print(n)

# DISCUSSION

# There isn't much more to regular expression search and replace than the sub() method shown. The trickiest part is
# specifying the regular expression pattern - something that's best left as an exercise to the reader.