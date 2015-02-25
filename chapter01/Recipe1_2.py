__author__ = 'Alessandro.Dantas'

"""
For example, suppose you run a course and decide at the end of the semester that you're going to drop the first and last
homework grades, and only average the rest of them. If there are only four assignments, maybe you simply unpack all four,
but what if there are 24? A star expression makes it easy:
 """

def drop_first_last(grades):
    first, *middle, last = grades
    print(middle)

grades = (8, 5, 5, 5, 5, 5, 10)

drop_first_last(grades)

"""
As another use case, suppose you have user records that consit of a name and email address, followed by an arbitrary
number of phone numbers. You could unpack the records like this:
"""

user_record = ('Dave', 'dave@example.com', '773-555-1212', '847-555-1212')
name, email, *phone_numbers = user_record
print(name)
print(email)
print(phone_numbers)

"""
It's worth noting that the phone_numbers variable will always be a list, regardless of how many phone numbers are
unpacked (including none). Thus, any code that uses phone_numbers won't have to account for the possibility that it
might not be a list or perform any kind of additional type checking.
"""


"""
The starred variable can also be the first one in the list. For example, say you have a sequence of values representing
your company's sale figures for the last eight quarters. If you want to see how the most recent quarter stacks up to the
average of the first seven, you could do something like this.
"""

*trailing, current = [10, 8, 7, 1, 9, 5, 10, 3]
print(trailing)
print(current)


"""
Extended iterable unpacking is tailor-made for unpacking iterables of unknown or arbitrary length. Oftentimes, these
iterables have some known component or pattern in their construction (e.g. "everything after element 1 is a phone
number"), and star unpacking lets the developer leverage those patterns easily instead of performing acrobatics to ge at
the relevant elements in the iterable.

It is worth noting that the star syntax can be specially useful when iterating over a sequence of tuples of varying
length.
"""

records = [
    ('foo', 1, 2),
    ('bar', 'hello'),
    ('foo', 3, 4),
]

def do_foo(x, y):
    print('foo', x, y)

def do_bar(s):
    print('bar', s)

for tag, *args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)


"""
Star unpacking can also be useful when combined with certain kinds of string processing operations, such as splitting.
"""

line = 'nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false'
uname, *fields, homedir, sh = line.split(':')
print(uname)
print(homedir)
print(sh)


"""
Sometimes you might want to unpack values and throw them away, You can't just specify a bare * when unpacking, but you
could use a common throwaway variable name, suca as _ or ign (ignored).
"""

record = ('ACME', 50, 123.45, (12, 18, 2012))
name, *_, (*_, year) = record
print(name)
print(year)

"""
There is a certain similarity between star unpacking and list-processing features of various functional languages. For
example, if you have a list, you can easily split it into head and tail components like this:
"""

items = [1, 10, 7, 4, 5, 9]
head, *tail = items
print(head)
print(tail)

