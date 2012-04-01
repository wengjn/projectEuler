#! /usr/bin/python
# filename: 47.py

'''
find the first four consecutive integers to have four distinct primes
factors. What is the first of these numbers?
it is wrong, maybe the factor function is wrong!!!!
'''
import math

def isPrime(n):
  if n==2: return True
  elif n==1: return False
  elif n%2==0: return False

  for i in xrange(3, int(math.sqrt(n)+1)):
    if n%i==0: return False
  return True

def factorize(n):
  if n==1:
    return []
  res = []
  while n%2==0:
    res.append(2)
    n //= 2
  limit = math.sqrt(n) + 1
  i = 3
  while i<=limit:
    if n%i==0:
      res.append(i)
      n //= i
      limit = math.sqrt(n+1)
    else:
      i += 2
  if n!=1:
    res.append(n)
  return res

def distinct_prime_factor(n):
  return set(factorize(n))

def main():
  facNum = 0
  n = 2*3*5*7 #starting number
  while facNum != 4:
    n += 1
    if len(distinct_prime_factor(n)) == 4: facNum += 1
    else: facNum = 0

  print n
  print n-3

if __name__ == '__main__':
  main()
