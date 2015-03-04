__author__ = 'Alessandro'

x = 1234
print(bin(x))  # Output: b10011010010
print(oct(x))  # Output: 0o2322
print(hex(x))  # Output: 0x4d2

"""
Alternatively, you can use the format() function if you don't want the 0b, 0o, or 0x prefixes to
appear. For example:
"""

print(format(x, 'b'))  # Output: 10011010010
print(format(x, 'o'))  # Output: 2322
print(format(x, 'x'))  # Output: 4d2

"""
Integers are signed, so if you are working with negative numbers, the output will also include a
sign. For example:
"""

x = -1234
print(format(x, 'b'))  # Output: -10011010010
print(format(x, 'x'))  # Output: -4d2

"""
If you need to produce an unsigned value instead, you'll need to add in the maximum value to set the
bit length. For example, to show a 32-bit value, use the following:
"""

x = -1234
print(format(2**32 + x, 'b'))  # Output: 11111111111111111111101100101110
print(format(2**32 + x, 'x'))  # Output: fffffb2e

"""
To convert integer string in different bases, simply use the int() function with an appropriate base.
For example:
"""

print(int('4d2', 16))         # Output: 1234
print(int('10011010010', 2))  # Output: 1234

"""
DISCUSSION

For the most part, working with binary, octal, and hexadecimal integers is straightforward. Just
remember that these conversions only pertain to the conversion of integers to and from a textual
representation. Under the covers, there's just one integer type.

Finally, there in one caution for programmers who use octal. The Python syntax for specifying octal
values is slightly different than many other languages. For example, if you try something like this,
you'll get a syntax error:
"""

import os
#os.chmod('Recipe3_4.py' 0755)  # Output: SyntaxError: invalid token

"""
Make sure you prefix the octal value with 0o, as shown here:
"""

os.chmod('Recipe3_4.py', 0o755)


