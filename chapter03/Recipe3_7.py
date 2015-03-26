__author__ = 'Alessandro.Dantas'

"""
Python has no special syntax to represent these floating-point values, but they can be created using float(). For
example:
"""

a = float('inf')
b = float('-inf')
c = float('nan')
print(a)
print(b)
print(c)

"""
To test for the presence of these values, use the math.isinf() and math.isnan() functions. For example:
"""

import math
print(math.isinf(a))
print(math.isnan(c))

"""
DISCUSSION

For more detailed information about these floating-point values, you should refer to the IEEE 754 specification. However,
there are a few tricky details to be aware of, especially related to comparisons and operators.

Infinite values will propagate in caluculations in a mathematical manner. For example:
"""

a = float('inf')
print(a + 45)
print(a * 10)
print(10 / a)

"""
However, certain operations are undefined and will result in a NaN result. For example:
"""

a = float('inf')
print(a/a)
b = float('-inf')
print(a + b)

"""
NaN values propagate through all operations without raising an exception. For example:
"""

c = float('nan')
print(c + 23)
print(c / 2)
print(c * 2)
math.sqrt(c)

"""
A subtle feature of NaN values is that they never compare as equal. For example:
"""

c = float('nan')
d = float('nan')
print(c == d)
print(c is d)

"""
Because of this, the only safe way to test for a NaN value is to use math.isnan(), as shown in this recipe.

Sometimes programmers want to change Python's behavior to raise exceptions when operations result in an infinite or NaN
result. The fpectl module can be used to adjust this behavior, but it is not enabled in a standard Python build, it's
platform-dependent, and really only intended for expert-level programmers.
"""

