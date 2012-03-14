#! /usr/bin/python
# filename: 3.py

# this is to calculate the largest prime factor of a number with many digit
# very good and fast method, copy from a guy name zacharydenton

# this one still need more thought

import math

def factorize(n):
  res = []
  #iterate over all even numbers first
  while n%2 == 0:
    res.append(2)
    n //= 2
  #try odd numbers up to sqrt(n)
  limit = math.sqrt(n+1)
  i = 3
  while i<limit:
    if n%i == 0:
      res.append(i)
      n //= i
      limit = math.sqrt(n+i)
    else:
      i += 2
  if n != 1:
    res.append(n)
  return res

print max(factorize(600851475143))

print max(factorize(13195))

