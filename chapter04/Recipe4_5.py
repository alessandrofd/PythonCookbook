__author__ = 'Alessandro.Dantas'

a = [1, 2, 3, 4]
for x in reversed(a):
    print(x)

# Reversed iteration only works if the object in question has a size that can be determined or if the object implements
# a __reversed__() special method. If neither of these can be satisfied, you'll have to convert the object into a list
# first. For example:

# Print a file backwards
f = open('somefile')
for line in reversed(list(f)):
    print(line, end='')

# Be aware that turning an iterable into a list as shown could consume a lot of memory if it's large

# DISCUSSION

# Many programmers don't realize that reversed iteration can be customized or user-defined classes if they implement the
# __reversed__() method. For example:

class Countdown:
    def __init__(self, start):
        self.start = start

    # Forward iterator
    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # Reverse iterator
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1

# Defining a reversed iterator makes the code much more efficient, as it's no longer necessary to pull the data inta a
# list and iterate in reverse on the list.

