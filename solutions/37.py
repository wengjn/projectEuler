#! /usr/bin/python
# filename: 37.py

'''
Find the sum of the only eleven primes that are both truncatable from 
left to right and right to left
'''

import math
import re

def isPrime(n):
  if n==1:
    return False
  if n==2:
    return True
  elif n%2==0:
    return False
  for i in range(3, int(math.sqrt(n)+1)):
    if n%i==0:
      return False

  return True

def main():
  # both from left to right and right to left
  total = 0
  count = 11
  i = 10
  while count !=0:
    i += 1
    if isPrime(i) and not re.search(r'0', str(i)):
      # from left to right
      # flag is used to denote how many prime here
      flag = 0
      for j in range(1, len(str(i))):
        if isPrime(int(str(i)[j:])):
          flag += 1 
      # from right to left
      for j in range(-1, -len(str(i)), -1):
        if isPrime(int(str(i)[:j])):
          flag += 1
      if flag == 2*(len(str(i))-1):
        total += i
        count -= 1
        print i

  print 'total:', total

if __name__ == '__main__':
  main()
