#! /usr/bin/python
# filename: 41.py

'''
What is the largest n-digit pandigital prime that exists.
There is one trick here, you should notice there is a huge set between 2143
and 987654321, which could make the program to be really slow.
So need to narrow down the set:
any integer is divisible by 3 or 9 whose sum of digits is divisble by 3 or9
therefore
sum('9,8,7,6,5,4,3,2,1')=45
sum('8,7,6,5,4,3,2,1')=36
sum('6,5,4,3,2,1')=21
sum('5,4,3,2,1')=15
It could only be in the 7 digits 
'''
import math

def isPandigital(n, s=9):
 n = str(n)
 return len(n) == s and not '1234567890'[:s].strip(n)


def isPrime(n):
  if n==1:
    return False
  if n==2:
    return True
  elif n%2==0:
    return False
  for i in xrange(3, int(math.sqrt(n)+1)):
    if n%i==0: return False
  return True

def main():
  for i in xrange(7654321, 2143, -2):
    if isPrime(i) and isPandigital(i,7):
      print i
      break



if __name__ == '__main__':
  main()
