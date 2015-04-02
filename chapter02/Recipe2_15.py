__author__ = 'Alessandro'

s = '{name} has {n} messages'
print(s.format(name='Guide', n=37))

# Alternatively, if the values to be substituted are truly found in variables, you can use the combination of
# format_map() and vars(), as in the following:

name = 'Guido'
n = 37
print(s.format_map(vars()))

# One subtle feature of vars() is that it also works with instances. For example:

class Info:
    def __init__(self, name, n):
        self.name = name
        self.n = n

a = Info('Guido', 37)
print(s.format_map(vars(a)))

# One downside of format() and format_map() is that they do not deal gracefully with missing values. For example:

#s.format(name='Guido')  # KeyError: 'n'

# One way to avoid this in to define as alternative dictionary class with a __missing__() method, as in the following:

class safesub(dict):
    def __missing__(self, key):
        return '{' + key + '}'

# Now use this class to wrap the inputs to format_map():

del n  # Make sure n is undefined
print(s.format_map(safesub(vars())))

# If you find yourself frequently performing these steps in your code, you could hide the variable substitution process
# behind a small utility function that employs a so-called "frame hack". For example:

import sys

def sub(text):
    return text.format_map(safesub(sys._getframe(1).f_locals))

# Now you can type things like this:

name = 'Guido'
n = 37
print(sub('Hello {name}'))
print(sub('You have {n} messages.'))
print(sub('Your favorite color is {color}'))

# DISCUSSION

# The lack of true variable interpolation in Python has led to a variety of solutions over the years. As an alternative
# to the solution presented in this recipe, you will sometimes see string formatting like this:

# name = 'Guido'
# n = 37
# '%(name) has %(n) messages.' % vars()


# You may also see the use of template strings:

import string
s = string.Template('$name has $n messages')
print(s.substitute(vars()))

# However, the format() and format_map() methods are more modern than either of these alternatives, and should be
# preferred. One benefit of using format() is that you also get all the features related to string formatting (alignment,
# padding, numerical formatting, etc.), which is simply not possible with alternatives such as Template string objects.

# Parts of this recipe also illustrate a few interesting advanced features. The little-known __missing__() method of
# mapping/dict classes is a method that you can define to handle missing values. In the safesub class, this method has
# been defined to return missing values back as a placeholder. Instead of getting a KeyError excepetion, you would see
# the missing values appear in the resulting string (potentially useful for debugging).

# The sub() function uses sys._getframe(1) to return the stack frame of the caller. From that, the f_locals attribute is
# accessed to get the local variables. It goes without saying that messing around with stack frames should probably be
# avoided in most code. However, for utility functions such as a string substitution feature, it can be useful. As an
# aside, it's probably worth noting that f_locals is a dictionary that is a copy of the local variables in the calling
# function. Although you can modify the contents fo f_locals, the modifications don't actually have any lasting effect.
# Thus, even though accessing a different stack frame might look evil, it's not possible to accidentally overwrite
# variables or change the local environment of the caller.

