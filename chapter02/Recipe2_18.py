__author__ = 'Alessandro'

# Suppose you have a string of text such as this:

text = 'foo = 23 + 42 * 10'

# To tokenize the string, you need to do more than merely match patterns. You need to have some way to identify the
# kind of pattern as well. For instance, you might want to turn the string into a sequence of pairs like this:

tokens = [('NAME', 'foo'), ('EQ', '='), ('NUM', '23'), ('PLUS', '+'), ('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

# To do this kind of splitting, the first step is to define all of the possible tokens, including whitespace, by regular
# expression patterns using named capture groups such as this:

import re
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ = r'(?P<EQ>=)'
WS = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# In these re patterns, the ?P<TOKENNAME> convention is used to assign a name to the pattern. This will be used later.

# Next, to tokenize, use the little-known scanner() method of pattern objects. This method creates a scanner object in
# which repeated calls to match() step through the supplied text one match at a time. Here is an interactive example of
# how a scanner object works:

# scanner = master_pat.scanner('foo = 42')
# scanner.match()
# print(_.lastgroup, _.group)
# scanner.match()
# print(_.lastgroup, _.group)
# scanner.match()
# print(_.lastgroup, _.group)
# ...

# To take this technique and put it into code, it can be cleaned up and easily packaged into a generator like this:

from collections import namedtuple

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

# Example use

for tok in generate_tokens(master_pat, 'foo = 42'):
    print(tok)

# If you want to filter the token stream in some way, you can either define more generator functions or use a generator
# expression. For example, here is how you might filter out all whitespace tokens.

print("===========")
tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)

# DISCUSSION

# Tokenizing is often the first step for more advanced kinds of text parsing and handling. To use the scanning techni-
# ques shown, there are a few important details to keep in mind. First, you must make sure that you identify every
# possible text sequence that might appear in the input with a corresponding re pattern. If any non-matching text is
# found, scanning simply stops. This is why it is necessary to specify the whitespace (WS) token in the example.

# The order of tokens in the master regular expression also matters. When matching, re tries to match patterns in the
# order specified. Thus if a pattern happens to be a substring of a longer pattern, you need to make sure the longer
# pattern goes first. For example:

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))  # Correct
#master_pat = re.compile('|'.join([LT, LE, EQ]))  # Incorrect

# The second pattern is wrong because it would match the text <= as the token LT followed by the token EQ, not the
# single token LE, as was probably desired.

# Last, but not least, you need to watch out for patterns that form substrings. For example, suppose you have two
# patterns like this:

PRINT = r'(?P<PRINT>print)'
NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME]))

for tok in generate_tokens(master_pat, 'printer'):
    print(tok)

# Outputs:
#   Token(type='PRINT', value='print')
#   Token(type='NAME', value='er')

# For more advanced kinds of tokenizing, you may want to check out packages such as PyParsing ou PLY. An example
# involving PLY appears in the next recipe.