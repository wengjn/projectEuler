#! /usr/bin/python
# filename: 19_2.py

# program from johnycoder.com
# good method
# python Dates and Times

# pleac.sourceforge.net/pleac_python/datesandtimes.html

import datetime

sundays = 0

for y in range(1901, 1902):
  for m in range(1, 13):
    # monday == 0, sunday == 6
    if datetime.datetime(y,m,1).weekday() == 6:
      sundays += 1

print sundays
