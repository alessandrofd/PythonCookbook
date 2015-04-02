__author__ = 'Alessandro'

s = "Look into my eyes, look into my eyes, the eyes, the eyes, \
the eyes, not around the eyes, don't look around the eyes, \
look into my eyes, you're under."

# Here's how you can use the textwrap module to reformat it in various ways:

import textwrap
print(textwrap.fill(s, 70))
print(textwrap.fill(s, 40))
print(textwrap.fill(s, 40, initial_indent='    '))
print(textwrap.fill(s, 40, subsequent_indent='    '))

# DISCUSSION

# The textwrap module is a straightforward way to clean up text for printing—especially if you want the output to fit
# nicely on the terminal. On the subject of the terminal size, you can obtain it using os.get_terminal_size().

# The fill method has a few additional options that control how it handles tabs, sentence endings, and so on.