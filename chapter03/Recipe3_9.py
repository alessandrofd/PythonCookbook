__author__ = 'Alessandro.Dantas'

"""
For any heavy computation involving arrays, use the NumPy library. The major feature of NumPy is that it gives Python an
array object that is much more efficient and better suited for mathematical calculation than a standard Python list.
Here is a short example illustrating important behavioral differences between lists and NumPy arrays:
"""

# Python lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
print(x * 2)
#print(x + 2) # TypeError: can only concatenate list (not "int") to list
print(x + y)

# Numpy
import numpy as np
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

"""
As you can see, basic mathematical operations involving arrays behave differently. Specifically, scalar operations
(e.g., ax * 2 or ax + 10) apply the operation on an element-by-element basis. In addition, performing math operations
when both operands are arrays applies the operation to all elements and produces a new array.

The fact that math operations apply to all of the elements simultaneously makes it very easy and fast to compute
functions across the entire array. For example, if you want to compute the value of a polynomial:
"""

def f(x):
    return 3*x**2 - 2*x + 7

print(f(ax))

"""
NumPy provides a collection of "universal functions" that also allow for array operations. These are replacements for
similar functions normally found int the math module. For example:
"""

print(np.sqrt(ax))
print(np.cos(ax))

"""
Using universal functions can be hundreds of times faster than looping over the array elements one at a time and
performing calculations using functions in the math module. Thus, you should prefer their use whenever possible.

Under the covers, NumPy arrays are allocated in the same manner as in C or Fortran. Namely, they are large, contiguous
memory regions consisting of homogenous data type. Because of this, it's possible to make arrays much larger than
anything you would normally put into a Python list. For example, if you want to make a two-dimensional grid of 10,000
by 10,000 floats, it's not an issue:
"""

grid = np.zeros(shape = (10000, 10000), dtype = float)
print(grid)

"""
All of the usual operations still apply to all of the elements simultaneously:
"""

grid += 10
print(grid)
#print(np.sin(grid))

"""
One extremely notable aspect of NumPy is the manner in which it extends Python's list indexing functionality - specially
with multidimensional arrays. To illustrate, make a simple two-dimensional array and try som experiments.
"""

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)

# Select row 1
print(a[1])

# Select column 1
print(a[:, 1])

# Select a subregion and change it
print(a[1:3, 1:3])
a[1:3, 1:3] += 10
print(a)

# Broadcast a row vector across an operation on all rows
print(a + [100, 101, 102, 103])
print(a)

# Conditional assignment on an array
print(np.where(a < 10, a, 10))

"""
DISCUSSION

NumPy is the foundation for a huge number of science and engineering libraries in Python. Is is also one of the larges
and most complicated modules in widespread use. That said, it's stil possible to accomplish useful things with NumPy by
starting with simple examples and playing around.

One note about usage is that it is relatively common to use the statement "import numpy as np", as shown in the solution.
This simply shortens the name to something that's more convenient to type over and over again in your program.
"""