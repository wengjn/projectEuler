#! /usr/bin/python
# filename: 27.py

'''
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n
n^2+an+b
a, b could be negative number
n^2+n+41, when n=40, divisible by 41, n=41, clearly divisable by 41
n^2-79n+1601,  
This guy has done a lot of work on how to find a and b, worth a look
http://blog.mycila.com/2009/05/project-euler-problem-27.html

'''
from collections import defaultdict
from itertools import product
from operator import mul
import math

def factorize(n):
  if n==1: return []
  res = []
  while n%2==0:
    res.append(2)
    n //= 2
  limit = math.sqrt(n)+1
  i = 3
  while i<= limit:
    if n%i==0:
      res.append(i)
      n //= i
      limit = math.sqrt(n+1)
    else:
      i += 2
  if n != 1:
    res.append(n)
  return res

def numDivisors(n):
  factors = sorted(factorize(n))
  histogram = defaultdict(int)
  for factor in factors:
    histogram[factor] += 1
  try:
    return reduce(mul, [exponent+1 for exponent in histogram.values()])
  except:
    return 1

def numPrimes(formula):
  num = 0
  for n in range(1000):
    res = formula(n)
    if res<1 or not isPrime(res):
      return num
    else:
      num += 1

def isPrime(n):
  if numDivisors(n) == 2 and n > 1:
    return True
  else:
    return False

def main():
  most = 0
  best = (0, 0)
  for a, b in product(range(-999, 1000), range(-999, 1000)):
    formula = lambda n: n**2 + a*n + b
    num = numPrimes(formula)
    if num > most:
      most = num
      best = (a, b)
  print mul(*best)

if __name__ == '__main__':
  main()
