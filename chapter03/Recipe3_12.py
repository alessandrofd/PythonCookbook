__author__ = 'Alessandro'

"""
To perform conversions and arithmetic involving different units of time, use the datetime module.
For example, to represent an interval of time, create a timedelta instance, like this:
"""

from datetime import timedelta
a = timedelta(days = 2, hours = 6)
b = timedelta(hours = 4.5)
c = a + b
print(c.days)
print(c.seconds)
print(c.seconds/3600)
print(c.total_seconds()/3600)

"""
From Python's documentation:

Only days, seconds, and microseconds are stored internally. Arguments are converted to those units:

    A millisecond is converted to 1,000 microseconds
    A minute is converted to 60 seconds.
    An hour is converted to 3,600 seconds
    A week is converted to 7 days.

and days, seconds, and microseconds are then normalized so that the representations is unique, with

    0 <= microseconds < 1,000,000
    0 <= seconds <= 3,600 * 24 (the number of seconds in one day)
    -999999999 <= days <= 999999999
"""

"""
If you need to represent specific dates and times, create datetime instances and use the standard
mathematical operations to manipulate them. For example:
"""

from datetime import datetime
a = datetime(2012, 9, 23)
print(a + timedelta(days = 10))

b = datetime(2012, 12, 21)
d = b - a
print(d.days)

now = datetime.today()
print(now)
print(now + timedelta(minutes=10))

"""
When making calculations, it should be noted that datetime is aware of leap years. For example:
"""

a = datetime(2012, 3, 1)
b = datetime(2012, 2, 28)
print(a - b)
print((a - b).days)

c = datetime(2013, 3, 1)
d = datetime(2013, 2, 28)
print((c - d).days)

"""
DISCUSSION

For most basic date and time manipulation problems, the datetime module will suffice. If you need to
perform more complex date manipulations, such as dealing with time zones, fuzzy time ranges,
calculating the dates of holidays, and so forth, look at the dateutil module.

To illustrate, many similar time calculations can be performed with the dateutil.relativedelta()
function. However, one notable feature is that it fills in some gaps pertaining to the handling of
months (and their differing number of days). For instance:
"""

a = datetime(2012, 9, 23)
#a + timedelta(months = 1)  # TypeError: 'months' is an invalid keyword argument for this function

from dateutil.relativedelta import relativedelta
print(a + relativedelta(months=+1))
print(a + relativedelta(months=+4))

# Time between two dates
b = datetime(2012, 12, 21)
d = b - a
print(d)

d = relativedelta(b, a)
print(d)
print(d.months)
print(d.days)