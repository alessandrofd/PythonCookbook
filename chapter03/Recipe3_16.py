__author__ = 'Alessandro'

"""
For almost any problem involving time zones, you should use the pytz module. This package provides
the Olson time zone database, which is the de facto standard for time zone information found in many
languages and operating systems.

A major use o pytz is in localizing simple dates created with the datetime library. For example,
here is how you would represent a date in Chicago time:
"""

from datetime import datetime
from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
print(d)

# Localize the date for Chicago
central = timezone('US/Central')
loc_d = central.localize(d)
print(loc_d)

"""
Once the date has been localized, it can be converted to other time zones. To find the same time in
Bangalore, you would do this:
"""

# Convert to Bangalore time
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))
print(bang_d)

"""
If you are going to perform arithmetic with localized dates, you need to be particularly aware of
daylight saving transitions and other details. For example, in 2013, U.S. standard daylight saving
time started on March 10, 2:00 a.m. local time (at which point, time skipped ahead one hour). If
you're performing native arithmetic, you'll get it wrong. For example:
"""

from datetime import timedelta

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
print(loc_d)
later = loc_d + timedelta(minutes=30)
print(later)

"""
The answer is wrong because it doesn't account for the one-hour skip in the local time. To fix it,
use the normalize() method of the time zone. For example:
"""

later = central.normalize(loc_d + timedelta(minutes=30))
print(later)

"""
DISCUSSION

To keep your head from completely exploding, a common strategy for localized date handling is to
convert all dates to UTC time and to use that for all internal storage and manipulation. For example:
"""

import pytz

print(loc_d)
utc_d = loc_d.astimezone(pytz.utc)
print(utc_d)

"""
Once in UTC, you don't have to worry about issues related to daylight saving time and other matters.
Thus, you can simply perform normal date arithmetic as before. Should you want to output the date
in localized time, just convert it to the appropriate time zone afterward. For example:
"""

later_utc = utc_d + timedelta(minutes=30)
print(later_utc.astimezone(central))

"""
One issue in working with time zones is simply figuring out what time zone names to use. For example,
in this recipe, how was it known that 'Asia/Kolkata' was the correct time zone name for India? To
find out, you can consult the pytz.country_timezones dictionary using the ISO 3166 country code as
a key. For example:
"""

print(pytz.country_timezones['IN'])

