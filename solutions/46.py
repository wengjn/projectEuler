#! /usr/bin/python
# filename: 46.py

'''
Goldbach conjecture was false
get the smallest odd composite that cannot be written as that type
odd composite is not prime number
This one is easy, but you need to notice that when to stop the while loop
'''
import math

def isPrime(n):
  if n==2: return True
  if n==1: return False
  elif n%2==0: return False

  for i in xrange(3, int(math.sqrt(n)+1)):
    if n%i==0: return False
  return True

def isSquare(n):
  m1 = int(math.sqrt(n))
  if m1 * m1 == n:
    return True
  return False

def main():
  primls = []
  for i in xrange(2, 10000):
    if isPrime(i): primls.append(i)

  n = 35 # start
  i = 0  # index of prime list
  while True:
    while primls[i] < n:
      temp = n - primls[i]
      if temp % 2 == 0:
        if isSquare(temp/2): 
          break
      i += 1
    # when to stop the while loop, if it ran out of all the prime it can use
    if primls[i] > n: 
      print n
      break
    n += 2
    if isPrime(n): n += 2
    i = 0


if __name__ == '__main__':
  main()
