__author__ = 'Alessandro'

# To manually consume an iterable, use the next() function and write your code to catch the StopIteration exception. For
# example, this example manually reads lines from a file:

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

# Normally, StopIteration is used to signal the end of iteration. However, if you're using next() manually (as shown),
# you can also instruct it to return a terminating value, such as None, instead. For example:

with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

# DISCUSSION

# In most cases, the for statement is used to consume an iterable. However, every now and then, a problem calls for more
# precise control over the underlying iteration mechanism. Thus, it is useful to know what exactly happens.

# The following interactive example illustrates the basic mechanics of what happens during iteration:

items = [1, 2, 3]
# Get the iterator
it = iter(items)  # Invokes items.__iter__()
# Run the iterator
next(it)          # Invokes it.__next__()
next(it)
next(it)
next(it)  # StopIteration

# Subsequent recipes in this chapter expand on iteration techniques, and knowledge of the basic iterator protocol is
# assumed. Be sure to tuck this first recipe away in your memory.
