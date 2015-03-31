__author__ = 'Alessandro.Dantas'


# This problem typically arises in patterns that use the dot (.) to match any character but forget to account for the
# fact that it doesn't match newlines. For example, suppose you are trying to match C-style comments:

import re
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a
              multiline comment */
'''
print(comment.findall(text1))
print(comment.findall(text2))

# To fix the problem, you can add the support for newlines. For example:

comment = re.compile(r'/\*((?:.|\n)*?)\*/')
print(comment.findall(text2))

# In this pattern. (?:.|\n) specifies a noncapture group (i.e., it defines a group for the purposes of matching, but
# that group is not captured separately or numbered).

# DISCUSSION

# The re.compile() function accepts a flag, re.DOTALL, which is useful here. It makes the . in a regular expression
# match all characters, including newlines. For example:

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
print(comment.findall(text2))

# Using the re.DOTALL flag works fine for simple cases, but it might be problematic if you're working with extremely
# complicated patterns or a mix of separate regular expressions that have been combined together for the purpose of
# tokenizing, as described in Recipe 2.18. If given a choice, it's usually better to define you regular expression
# pattern so that it works correctly without the need of extra flags.