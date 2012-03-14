#! /usr/bin/python
# filename: 12_2.py

# this is a program from others
# mine is too too slow

import time
import math

start = time.time()

def divisor_count(x):
  count = 2 
  for i in xrange(2, int(math.sqrt(x))+1):
    if ((x%i)==0):
      if(i != math.sqrt(x)): count += 2
      else: count += 1

  return count

def triangle_generator():
  i = 1
  while True:
    yield int(0.5*i*(i+1))
    i += 1

triangles = triangle_generator()

answer = 0
while True:
  num = triangles.next()
  if (divisor_count(num) >= 501):
    answer = num
    break
print answer
print 'elapsed time:', (time.time()-start)*1000, 'millisecs'
a = raw_input('press return to continue')

