#! /usr/bin/python
# filename: 10.py

# find all the primes
# just for the test of git
#kek
import math

def isPrime(n):
  if n == 2:
    return True
  elif n%2 == 0:
    return False

  for i in range(3, int(math.sqrt(n))+1):
    if n%i == 0:
      return False
    i += 1

  return True

def main():
  N, T = 2, 3

  while T < 2000000:
    if isPrime(T):
      N += T
    T += 2  

  print N


if __name__=='__main__':
  main()
