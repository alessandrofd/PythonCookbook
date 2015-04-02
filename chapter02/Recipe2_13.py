__author__ = 'Alessandro'

text = 'Hello World'
print('[' + text.ljust(20) + ']')
print('[' + text.rjust(20) + ']')
print('[' + text.center(20) + ']')

# All of these methods accept an optional fill character as well. For example:

print('[' + text.rjust(20, '=') + ']')
print('[' + text.center(20, '*') + ']')

# The format() function can also be used to easily align things. All you need to do is use the <, >, or ^ characters
# along with a desired width. For example:

print('[' + format(text, '>20') + ']')
print('[' + format(text, '<20') + ']')
print('[' + format(text, '^20') + ']')

# If you want to include a fill character other than a space, specify it before the alignment character:

print('[' + format(text, '=>20s') + ']')
print('[' + format(text, '*^20s') + ']')

# These format codes can also be used in the format() method when formatting multiple values. For example:

print('[' + '{:>10s} {:>10s}'.format('Hello', 'World') + ']')

# One benefit of format() is that it is not specific to strings. It works with any value, making it more general purpo-
# se. For instance, you can use it with numbers:

x = 1.2345
print('[' + format(x, '>10') + ']')
print('[' + format(x, '^10.2f') + ']')

# DISCUSSION

# In older code, you will also see the % operator used to format text. For example:

print('[' + '%-20s' % text + ']')
print('[' + '%20s' % text + ']')

# However, in new code, you should probably prefer the use of the format() function or method. format() is a lot more
# powerful than what is provided with the % operator. Moreover, format() is more general purpose than using the ljust(),
# rjust(), or center() method of strings in that it works with any kind of object.
