__author__ = 'Alessandro'

"""
Python's datetime module has utility functions and classes to help perform calculations  like this.
A decent, generic solution to this problem looks like this:
"""

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days = days_ago)
    return target_date

print(datetime.today())  # For reference
print(get_previous_byday('Monday'))
print(get_previous_byday('Sunday'))  # Previous week, not today
print(get_previous_byday('Friday'))

"""
The optional start_date can be supplied using another datetime instance. For example:
"""

print(get_previous_byday('Sunday', datetime(2012, 12, 21)))

"""
DISCUSSION

This recipe works by mapping the start date and the target date to their numeric position in the
week (with Monday as day 0). Modular arithmetic is then used to figure out how many days ago the
target date last occurred. From there, the desired date is calculated from the start date by
subtracting an appropriate timedelta instance.

If you're performing a lot of date calculations like this, you may be better off installing the
python-dateutil package instead. For example, here is as example of performing the same calculation
using the relativedelta() function from dateutil:
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta
from dateutil.rrule import *

d = datetime.now()
print(d)

# Next Friday
print(d + relativedelta(weekday = FR))

# Last Friday
print(d + relativedelta(weekday = FR(-1)))
