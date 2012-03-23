#! /usr/bin/python
# filename: 35.py

'''
How many circular primes are there below one million?
197,971,719are themselves prime
prime number
the key problem is how to get circular number
not so hard! got it!
'''
import math

def isPrime(n):
  '''determine if the number n is a prime number or not'''
  if n == 2:
    return True
  elif n%2 == 0:
    return False

  for i in range(3, int((math.sqrt(n)+1))):
    if n%i == 0:
      return False

  return True

def main():
  # include 13 primes 2,3,5,7,11,13,17,31,37,71,73,79,97
  count = 13 
  for i in xrange(100, 1000000):
    # first determine if i is prime or not, if it is, continue
    if isPrime(i):
      temp = str(i)[1:] + str(i)[0]
      flag = 0
      for j in xrange(0, len(str(i))):
        if isPrime(int(temp)):
          temp = str(temp)[1:] + str(temp)[0]
          flag += 1
        else: 
          break
      if flag == len(str(i)): count += 1

  print count



if __name__=='__main__':
  main()
