__author__ = 'Alessandro'

s = 'Elements are written as "<tag>text</tag>".'
import html
print(s)
print(html.escape(s))

# Disable escaping of quotes
print(html.escape(s, quote=False))


# If you're trying to emit text as ASCII and want to embed character code entities for non ASCII characters, you can
# use the errors='xmlcharrefreplace' argument to various I/O-related functions to do it. For example:

s = 'Spicy Jalapeño'
print(s.encode('ascii', errors='xmlcharrefreplace'))

# To replace entities in text, a different approach is needed. If you're actually processing HTML or XML, try using a
# proper HTML or XML parser first. Normally, these tools will automatically take care of replacing the values for you
# during parsing and you don't need to worry about it.

# If, for some reason, you've received bare text with some entities in it and you want them replaced manually, you can
# usually do it using various utility functions/methods associated with HTML or XML parsers. For example:

s = 'Spicy &quot;Jalape&#241;o&quot.'
from html.parser import HTMLParser
p = HTMLParser()
print(p.unescape(s))

t = 'The prompt is &gt;&gt;&gt;'
from xml.sax.saxutils import unescape
print(unescape(t))

# DISCUSSION

# Proper escaping of special characters is an easily overlooked detail of generating HTML or XML. This is specially tru
# if you're generating such output yourself using print() or other basic string formatting features. Using an utility
# such as html.escape() is as easy solution.

# If you need to process text in the other direction, various utility functions, such as xml.sax.saxutils.unescape(),
# can help. However, you really need to investigate the use of a proper parser. For example, if processing HTML or XML,
# using a parsing module such as html.parser or xml.etree.ElementTree should already take care of details related to
# replacing entities in the input text for you.