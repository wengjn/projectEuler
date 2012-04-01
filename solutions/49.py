#! /usr/bin/python
# filename: 49.py

'''
what 12-digit number do you form by contatenating the three terms in this
sequence
'''
import math
import re

def isPrime(n):
  if n==2: return True
  elif n%2==0: return False
  for i in xrange(3, int(math.sqrt(n)+1)):
    if n%i==0: return False
  return True

def isPan(n):
  '''if this 4-digit number is composed only by distinct numbers'''
  s = str(n)
  for i in xrange(0, 4):
    ss = s[i]
    mat = re.findall(ss, s)
    if len(mat)>=2:  return False
  return True

def isPermu(s1, s2):
  for i in xrange(0, 4):
    if str(s1)[i] not in str(s2): return False
  return True

def main():
  n = 1489
  while True:
    b, c = n+3330, n+6660
    if isPrime(n) and isPrime(b) and isPrime(c) \
        and isPermu(n, b) and isPermu(b, c):
      break
    n += 2

  print n, b, c
  print str(n) + str(b) + str(c)

if __name__ == '__main__':
  main()

