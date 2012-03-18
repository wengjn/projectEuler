#! /usr/bin/python
# filename: 19.py

# first I was wrong at firstDay(n)
# It should be like days%7+1, it should be like days%7
# import calendar
# cal = calendar(1901, 1)
# print cal

# How many Sundays fell on the first of the month during the twentieth 
# century (1 Jan 1901 to 31 Dec 2000)

# 30 days: (4) April, June, September, November
# 31 days: (7) Jan, March, May, July, August, Oct, Dec
# 28 or 29 days: Feb
# initially, Jan 1, 1900 is a Monday
# end, Dec, 31, 2000

# see if this year is leap year or not
def leapYear(n):
  if n%4 == 0 and n%400 != 0:
    return True
  else: 
    return False

def firstDay(n):
  days = 0
  for i in range(1900, n):
    if leapYear(i):
      days += 366
    else:
      days += 365
  return (days%7)

# not true: count sundays in the first month of year n
# true: count++, if this sunday fall in the first of that month
def sundays(n):
  count = 0
  first = firstDay(n)
  day31 = [3, 5, 7, 8, 10, 12]
  leap = leapYear(n)
  if first == 7 or first == 0:
    count += 1
  # for Feb
  if ((first+31)%7) == 0:
    count += 1
  # from March to Dec
  total = 0
  if leap:
    total = first + 31 + 29
  else:
    total = first + 31 + 28

  for i in range(3, 13):
    if (total%7) == 0: count += 1
    if i in day31:
      total += 31
    else:
      total += 30

  return count

def main():
  count = 0
  for i in range(1901, 2001):
    count += sundays(i)

  print count

if __name__ == '__main__':
  main()
