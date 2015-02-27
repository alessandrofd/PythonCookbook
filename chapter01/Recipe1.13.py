__author__ = 'Alessandro.Dantas'
"""
Let's say you've queried a database table to get a listing of the members on your website, and you receive the following
data structures in return:
"""

rows = [
    {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
    {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
    {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
    {'fname': 'Big', 'lname':'Jones', 'uid': 1004}
]

"""
It's fairly easy to output these rows ordered by any of the fields common to all of the dictionaries. For example:
"""
from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))

print(rows_by_fname)
print(rows_by_uid)

"""
The itemgetter() function can also accept multiple keys. For example, this code
"""

rows_by_lfname = sorted(rows, key=itemgetter('lname', 'fname'))
print(rows_by_lfname)

"""
DISCUSSION

In this example, rows is passed to the built-in sorted() function, which accepts a keyword argument key. This argument
is expected to be a callable that accepts a single item from rows as input and returns a value that will be used as
basis for sorting. The itemgetter() function creates just such a callable.

The operator.itemgetter() function takes as arguments the lookup indices used to extract the desired values from the
records in rows. It can be a dictionary key name, a numeric list element, or any value that can be fed into an object's
__getitem__() method. If you give multiple indices to itemgetter(), the callable it produces will return a tuple with
all of the elements in it, and sorted() will order the output according to the sorted order of the tuples. This can be
useful if you want to simultaneously sort on multiple fields (such as last and first name, as show in the example).
"""

"""
The functionality of itemgetter() is sometimes replaced by lambda expressions. For example:
"""

rows_by_fname = sorted(rows, key=lambda r: r['fname'])
print(rows_by_fname)

rows_by_lfname = sorted(rows, key=lambda r: (r['lname'], r['fname']))
print(rows_by_lfname)

"""
This solution often works just fine. However, the solution involving itemgetter() typically runs a bit faster. Thus, you
might prefer it if performance is a concern.

Last, but not least, don't forget that the technique shown in this recipe can be applied to functions such as min() and
max(). For example:
"""

print(min(rows, key=itemgetter('uid')))
print(max(rows, key=itemgetter('uid')))

