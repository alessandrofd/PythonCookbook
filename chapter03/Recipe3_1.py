__author__ = 'Alessandro.Dantas'

print(round(1.23, 1))
print(round(1.27, 1))
print(round(-1.27, 1))
print(round(1.25361, 3))

"""
When a value is exactly halfway between two choices, the behavir of round is to round to the nearest even digit. That
is, values such as 1.5 or 2.5 both get rounded to 2.

The number of digits given to round() can be negative, in which case rounding takes place for tens, hundreds, thousands,
and son on. For example:
"""

a = 1627731
print(round(a, -1))
print(round(a, -2))
print(round(a, -3))

"""
DISCUSSION

Don't confuse rounding with formatting a value for output. If your goal is simply to output a numerical value with a
certain number of decimal places, you don't typically need to use round(). Instead, just specify the desired precision
when formatting. For example:
"""

x = 1.23456
print(format(x, '0.2f'))
print(format(x, '0.3f'))
print('value is {:0.3f}'.format(x))
