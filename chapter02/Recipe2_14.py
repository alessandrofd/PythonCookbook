__author__ = 'Alessandro'

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
print(' '.join(parts))
print(','.join(parts))
print(''.join(parts))

# At first glance, this syntax might look really odd, but the join() operation is specified as a method on strings.
# Partly this is because the objects you want to join could come from any number of different data sequences (e.g,
# lists, tuples, dicts, files, sets, or generators), and it would be redundant to have join() implemented as a method on
# all of those objects separately. So you just specify the separator string that you want and use the join() method on
# it to glue text fragments together.

# If you're only combining a few strings, using + usually works well enough:

a = "Is Chicago"
b = "Not Chicago?"
print (a + ' ' + b)

# The + operator also works fine as a substitute for more complicated string formatting operations. For example:

print('{} {}'.format(a, b))
print(a + ' ' + b)

# If you're trying to combine string literals together in source code, you can simply place them adjacent to each other
# with no + operator. For example:

a = 'Hello' 'World'
print(a)

# DISCUSSION

# Joining strings together might not seem advanced enough to warrant an entire recipe, but it's often an area where pro-
# grammers make programming choices that severely impact the performance of their code.

# The most important thing to know is that using the + operator to join a lot of strings together is grossly inefficient
# due to the memory copies and garbage collection that occurs. In particular, you never want to write code that joins
# strings together like this:

s = ''
for p in parts:
    s += p
print(s)

# This runs quite a bit slower than using join() method, mainly because each += operation creates a new string object.
# You're better off just collecting all of the parts first and then joining them together at the end.

# One related (and pretty neat) trick is the conversion of data to strings and concatenation at the same time using a
# generator expression, as described in Recipe 1.19. For example:

data = ['ACME', 50, 91.1]
print(','.join(str(d) for d in data))

# Also be on the lookout for unnecessary sting concatenations. Sometimes programmers get carried away with concatenation
# when it1s really not technically necessary. For example, when printing:

a = 'Is'
b = 'it'
c = 'necessary?'

print(a + ':' + b + ':' + c)  # Ugly
print(':'.join([a, b, c]))    # Still ugly
print(a, b, c, sep=':')       # Better

# Mixing I/O operations and string concatenation is something that might require study in your application. For example,
# consider the following two code fragments:

# Version 1 (string concatenation)
# f.write(chunk1 + chunk2)

# Version 2 (separate I/O operations)
# f.write(chunk1)
# f.write(chunk2)

# If two strings are small, the first version might offer much better performance due to the inherent expense of
# carrying out an I/O system call. On the other hand, if the two strings are large, the second version may be more
# efficient, since it avoids making a large temporary result and copying large blocks of memory around. Again, it must
# be stressed that this is something you would have to study in relation to your own data in order to determine which
# performs best.

# Last, but not least, if you're writing code that is building output from lots of small strings, you might consider
# writing that code as a generator function, using yield to emit fragments. For example:

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

# The interesting thing about this approach is that it makes no assumption about how the fragments are to be assembled
# together. For example, you could simply join the fragments using join():

text = ''.join(sample())
print(text)

# Or you could redirect the fragments to I/O:

# for part in sample:
#     f.write(part)

# Or you could come up with some kind of hybrid scheme that's smart about combining I/O operations:

def combine(source, maxsize):
    parts = [ ]
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    f.write(part)

# The key point is that the original generator function doesn't have to know the precise details. It just yields the
# parts.

