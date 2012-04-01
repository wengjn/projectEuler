#! /usr/bin/python
# filename: 45.py

'''
Find the next triangle number that is also pentagonal and hexagonal
the idea is easy, but could run really really slow
note that hexagonal num are a subset of triangle

import math

def isHexagonal(n):
  if n == 1: return True
  elif n == 0: return False
  limit = int(math.sqrt(n/2))+1
  i = limit
  while i >= (limit-1):
    if n == i*(2*i-1): return True
    i -= 1
  return False

def isPentagonal(n):
  if n == 1 or n == 5: return True
  elif n == 0: return False
  limit = int(math.sqrt(2*n/3)) + 1
  i = limit
  while i >= (limit-1):
    if 2*n == i*(3*i-1): return True
    i -= 1
  return False

def isTriangle(n):
  if n == 1: return True
  elif n == 2 or n == 0: return False
  limit = int(math.sqrt(n*2))
  i = limit
  while i>=limit-1:
    if 2*n == i*(i+1): return True
    i -= 1
  return False

def main():
  i = 407555
  while True:
    if isHexagonal(i) and isPentagonal(i) :
      print i
      break
    i += 1

Another good way:
from math import sqrt
for x in range(285, 100000):
  c = (x**2+x)/2
  y = (.5 + sqrt(.25+6*c))/3
  z = (1+sqrt(1+8*c))/4
  if y == int(y) and z == int(z):
    print x, y, z
'''

from math import sqrt

def isPantagonal(n):
  p = (sqrt(1+24*n)+1)/6
  return p == int(p)

h = lambda n: n*(2*n - 1) # calculate the nth hexagonal num

n = 144
while not(isPantagonal(h(n))): n += 1

print h(n)

