__author__ = 'Alessandro.Dantas'

"""
The fractions module can be used to perform mathematical calculations involving fractions. For example:
"""

from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
print(a * b)

# Getting numerator/denominator
c = a * b
print(c.numerator)
print(c.denominator)

# Converting to a float
print(float(c))

# Limiting the denominator of a value
print(c.limit_denominator(8))

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)

"""
DISCUSSION

Calculation with fractions doesn't arise often in most programs, but there are situations where it might make sense to
use them. For example, allowing a program to accept units of measurement in fractions and performing calculations with
them in that form might alleviate the need for a user to manually make conversions to decimals or floats.
"""