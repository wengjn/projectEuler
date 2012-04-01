#! /usr/bin/python
# filename: 43.py

'''
Find the sum of all 0 to 9 pandigital numbers with a good property
key is how to get this pandigital, different from before.
a good mathematical analysis is here:
http://blog.singhanuvrat.com/problems/project-euler-43-pandigital-numbers-with-unusual-substring-divisibility-property

'''
from itertools import *

def hasProperty(digits):
  primes = [1, 2, 3, 5, 7, 11, 13, 17]
  for i in xrange(1, 8):
    if not int(''.join(digits[i:i+3])) % primes[i] ==0:
      return False
  return True

def convertListToInt(l):
  return int(''.join(str(i) for i in l))


def main():
  pandigitals = permutations((str(i) for i in range(10)))
  print sum(convertListToInt(p) for p in pandigitals if hasProperty(p))

if __name__ == '__main__':
  main()
