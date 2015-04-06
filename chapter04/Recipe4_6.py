__author__ = 'Alessandro.Dantas'

# Recipe 4.6. Defining Generator Function with Extra State
#
#     Problem: You would like to define a generator function, but it involves extra state that you would like to expose
#       to the user somehow.
#
#     Solution: If you want a generator to expose extra stat to the user, don't forget that you can easily implement it
#       as a class, putting the generator function code in the __iter__() method.


from collections import deque

class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()

# To use this class, you would treat it like a normal generator function. However, since it creates an instance, you can
# access internal attributes, such as the history attribute or the clear() method. For example:

with open('somefile') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno, hline in lines.history:
                print('{}:{}'.format(lineno, hline), end='')


# DISCUSSION

# With generators, it is easy to fall into a trap of trying to do everything with functions alone. This can lead to
# rather complicated code if the generator function needs to interact with other parts of your program in unusual ways
# (exposing attributes, allowing control via method calls, etc.). If the is the case, just use a class definition, as
# shown. Defining your generator in the __iter__() method doesn't change anything about how you write your algorithm.
# The fact that it's part of a class makes it easy for you to provide attributes and methods for users to interact with.

# One potential subtlety with the method shown is that it might require an extra step of calling iter() if you are going
# to drive iteration using a technique other than a for loop. For example:

f = open('somefile')
lines = linehistory(f)
#next(lines) # TypeError: 'linehistory' object is not an iterator

# Call iter() first, then start iterating
it = iter(lines)
print(next(it))
print(next(it))


