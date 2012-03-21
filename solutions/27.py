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
import math

def isPrime(n):
  for x in range(2, int(math.sqrt(n))+1):
    if n%x==0: return False
  return True

def main():


if __name__ == '__main__':
  main()
