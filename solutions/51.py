#! /usr/bin/python
# filename: 51.py

'''
Find the smallest prime which, by changing the same part of the number
can form eight different primes
56003, 56113, 56333, ...
not necessary adjacent digits
This one is harder than I thought!!!
'''
import math

def isPrime(n):
  if n==2: return True
  elif n%2==0: return False
  i = 3
  while i<int(math.sqrt(n)+1):
    if n % i == 0: return False
    i +=  1

  return True

def main():


if __name__ == '__main__':
  main()
