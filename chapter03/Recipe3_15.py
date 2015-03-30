__author__ = 'Alessandro'

"""
Python's standard datetime module is typically the easy solution for this. For example:
"""

from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')
z = datetime.now()
diff = z - y
print(diff)

"""
DISCUSSION

The datetime.strptime() method supports a host of formatting codes. like %Y for the four-digit year
and the %m for the two-digit month. It's also worth noting that these formatting placeholders also
work in reverse, in case you need to represent a datetime object in string output and make it look
nice.

For example, let's say you have some code that generates a datetime object, but you need to format
a nice, human-readable date to put in the header of an auto-generated letter or report:
"""

print(z)
nice_z = datetime.strftime(z, '%A %B %d, %Y')
print(nice_z)

"""
It's worth noting that the performance of strptime() is often much worse than you might expect, due
to the fact that it's written in pure Python and it has to deal with all sorts of system locale
settings. If you are parsing a lot of dates in your code and you know the precise format, you will
probably get much better performance by cooking up a custom solution instead. For example, if you
knew that the dates were of the form 'YYYY-MM-DD', you could write a function like this:
"""

from datetime import datetime

def parse_ymd(s):
    year_s, month_s, day_s = s.split('-')
    return datetime(int(year_s), int(month_s), int(day_s))

"""
When tested, this function runs over seven times faster that datetime.strptime(). This is probably
something to consider if you're processing large amounts of data involving dates.
"""