__author__ = 'Alessandro.Dantas'

"""
Complex number can be specified using the complex(real, imag) function or by floating-point numbers with a j suffix. For
example:
"""

a = complex(2, 4)
b = 3 - 5j
print(a)
print(b)

"""
The real, imaginary, and conjugate values are easy to obtain, as shown here:
"""

print(a.real)
print(a.imag)
print(a.conjugate())

"""
In addition, all of the usual mathematical operators work:
"""

print(a + b)
print(a * b)
print(a / b)
print(abs(a))

"""
To perform additional complex-valued functions such as sines, cosines, or square roots, use the cmath module.
"""

import cmath
print(cmath.sin(a))
print(cmath.cos(a))
print(cmath.exp(a))

"""
DISCUSSION

Most of Python's math-related modules are aware of complex values. For example, if you use numpy, it is straightforward
to make arrays of complex values and perform operations on them:
"""

import numpy as np
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
print(a)
print(a + 2)
print(np.sin(a))

"""
Python's standard mathematical functions do not produce complex values by default, so it is unlikely that such a value
would accidentally show up in your code. For example:
"""

import math
# math.sqrt(-1)  # ValueError: math domain error

"""
If you want complex numbers to be produced as a result, you have to explicitly use cmath or declare the use of a complex
type in libraries that know about them. For example:
"""

import cmath
print(cmath.sqrt(-1))