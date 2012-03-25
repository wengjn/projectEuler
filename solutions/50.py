#! /usr/bin/python
# filename: 50.py

'''
which prime, below one-million, can be written as the sum of the most
consecutive primes
This is not a hard problem. first to generate a list of summing all primes
up to 1000,000, then two loops through these num.
'''
import math

def isPrime(n):
  if n==1: return False
  elif n==2: return True
  elif n%2==0: return False
  for i in xrange(3, int(math.sqrt(n))+1):
    if n%i == 0: return False

  return True

def main():
  res = [2]
  i = 3
  # generate a list of summing all primes up to 1000,000
  while res[-1] < 1000000:
    if isPrime(i):
      res.append(i + res[-1])
    i += 2

  # search for the greates sum, which is prime
  maxinum = 0
  for j in xrange(len(res)):
    for k in xrange(j,len(res)):
      temp = res[k] - res[j]
      num = k - j
      if isPrime(temp) and num > maxinum:
        maxinum = num
        primeNeed = temp
  print primeNeed
  print maxinum

if __name__ == '__main__':
  main()
