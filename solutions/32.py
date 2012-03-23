#! /usr/bin/python
# filename: 32.py

'''
Find the sum of all products whose multiplicand/multiplier/product identity
can be written as 1 through 9 pandigital
No clue for this problem at first
A set is used to ignore duplicate products.
another good way:
''.join(sorted(str(a)+str(b)+str(c)))=='123456789'
'''

def isPandigital(n, s=9):
  n = str(n)
  return len(n)==s and not '1234567890'[:s].strip(n)

def main():
  p = set()

  for i in xrange(2, 100):
    start = 1234
    if i>9: start=123
    for j in xrange(start, 10000/i+1):
      if isPandigital(str(i)+str(j)+str(i*j)): p.add(i*j)

  print sum(p)

if __name__ == '__main__':
  main()
