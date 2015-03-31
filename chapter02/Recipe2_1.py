__author__ = 'Alessandro.Dantas'

"""
The split() method of string objects is really meant for very simple case, and does not allow for multiple delimiters or
account for possible whitespace around the delimiters. In cases when you need a bit more flexibility, use the re.split()
method.
"""

line = "asdf fjdk; afed, fjek,asdf,        foo"
import re
print(re.split(r'[;,\s]\s*', line))

"""
DISCUSSION

The re.split() function is useful because you can specify multiple patterns for the separator. For example, as shown in
the solution, the separator is either a comma (,), a semicolon (;), or a whitespace followed by any amount of extra
whitespace. Whenever that pattern is found, the entire match becomes the delimiter between whatever fields lie on either
side of the match. The result is a list of fields, just as with str.split().

When using re.split(), you need to be a bit careful should the regular expression pattern involve a capture group
enclosed in parentheses. If capture groups are used, then the matched text is also included in the result. For example,
watch what happens here:
"""

fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

"""
Getting the split characters might be useful in certain contexts. For example, maybe you need the split characters later
on to reform an output string:
"""

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

"""
From Python Central - http://www.pythoncentral.io/cutting-and-slicing-strings-in-python/

...
Slicing Python Strings
Before that, what if you want to extract a chunk of more than one character, with known position and size? That's fairly
easy and intuitive. We extend the square-bracket syntax a little, so that we can specify not only the starting point,
but also where it ends.
"""

s = 'Don Quijote'
print(s[4:8])

"""
Let's look at what's happening here. Just as before, we're specifying that we want to start at position 4 (zero-based)
in the string. But now, instead of contenting ourselves with a single character from the string, we're saying that we
want more characters, up to **but not including** the character at position 8.

You might have thought that you were going to get the character at position 8 too. But that's not the way it works.
Don't worry - you'll get used to it. If it helps, thing of the second index (the one **after** the colon) as specifying
the first character that you **don't** want. Incidentally, a benefit of this mechanism is that you can quickly tell how
many characters you are going to end up with simply by subtracting the first index from the second.

Using this syntax, you can omit either or both of the indices. The first index, if omitted defaults to 0, so that your
chunk starts from the beginning of the original string; the second defaults to the highest position in the string, so
that your chunk ends at the end of the original string. Omitting both indices isn't likely to be of much practical use;
as you might guess, it simply returns the whole of the original string.
"""

print(s[4:])
print(s[:4])
print(s[:])

# Reform the line using the same delimiters
print(''.join(v+d for v, d in zip(values, delimiters)))

"""
If you don't want the separator characters in the result, but still need to use parentheses to group parts of the
regular expression pattern, make sure you use a noncapture group, specifeid as (?:...). For example:
"""

fields = re.split(r'(?:,|;|\s)\s*', line)
print(fields)
