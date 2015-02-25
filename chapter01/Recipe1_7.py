__author__ = 'Alessandro'

from collections import OrderedDict

d = OrderedDict()
d['foo'] = 1
d['bar'] = 2
d['spam'] = 3
d['grok'] = 4

# Outputs "foo 1", "bar 2", "spam 3", "grok 4"
for key in d:
    print(key, d[key])

"""
An OrderedDict can be particularly useful when you want to build a mapping that you may want to later
serialize or encode into a different format. For example, if you want to precisely control the order
of the fields appearing in a JSON encoding, first building the data in an OrderedDict will do the trick:
"""

import json
print(json.dumps(d))

"""
DISCUSSION

An OrderedDict internally maintains a doubly linked linked list that orders the keys according to
insertion order. When a new item is first inserted, it is placed at the end of this list. Subsequent
reassignment of an existing key doesn't change the order.

Be aware that the size of an OrderedDict is more than twice as large as a normal dictionary due to the
extra linked list that's created. Thus, if you are going to build a data structure involving a large
number of OrderedDict instances (e.g., reading 100,000 lines of a CSV file into a list of OrderedDict
instances), you would need to study the requirements of your application to determine if the benefits
of using an OrderedDict outweighed the extra memory overhead.
"""
