__author__ = 'Alessandro.Dantas'

"""
To illustrate, let's say you have a list of words and you want to find out which words occur most often. Here's how you
would do it:
"""

words = [
    'look', 'intro', 'my', 'eyes', 'look', 'my', 'eyes',
    'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
    'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
    'my', 'eyes', "you're", 'under'
]

from collections import Counter
word_counts = Counter(words)
top_three = word_counts.most_common(3)
print(top_three)

"""
DISCUSSION

As input, Counter objects can be fed any sequence of hashable input items. Under the covers, a Counter is a dictionary
that maps the items to the number of occurrences. For example:
"""

print(word_counts['not'])
print(word_counts['eyes'])

"""
If you want to increment the count manually, simply use addition:
"""

morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'eyes']
for word in morewords:
    word_counts[word] += 1

print(word_counts['eyes'])

"""
Or, alternatively, you could use the update() method:
"""

word_counts.update(morewords)
print(word_counts['eyes'])

"""
A little-known feature of Counter instances is that they can be easily combined using various mathematical operations.
For example:
"""

a = Counter(words)
b = Counter(morewords)
print(a)
print(b)
# Combine counts
c = a + b
print(c)
# Subtract counts
d = a - b
print(d)

"""
Needless to say, Counter objects are a tremedously useful tool for almost any kind of problem where you need to tabulate
and count data. You should prefer this over manually written solutions involving dictionaries.
"""
