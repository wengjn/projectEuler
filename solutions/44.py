#! /usr/bin/python
# filename: 44.py

'''
Find the pair of pentagonal numbers
'''
from itertools import *
from math import *
from operator import *

def pentagonal(n):
  return n*(3*n-1)/2

def main():
  pentagonals = set(pentagonal(n) for n in xrange(1, 3000))
  c = combinations(pentagonals, 2)
  for p in c:
    if add(*p) in pentagonals and abs(sub(*p)) in pentagonals:
      print abs(sub(*p))

if __name__ == '__main__':
  main()
