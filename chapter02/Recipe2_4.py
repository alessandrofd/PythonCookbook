__author__ = 'Alessandro'

# If the text you're trying to match is a simple literal, you can often just use the basic string
# methods, such as str.find(), str.endswith(), str.startswith(), or similar.

text = 'yeah, but no, but yeah, but no, but yeah'

# Exact match
print(text == 'yeah')

# Match at start or end
print(text.startswith('yeah'))
print(text.endswith('no'))

# Search for the location of the first occurrence
print(text.find('no'))

# For more complicated matching, use regular expressions and the re module. To illustrate the basic
# mechanics of using regular expressions, suppose you want to match dates specified as digits, such
# as "11/27/2012". Here is a sample of how you would do it.


