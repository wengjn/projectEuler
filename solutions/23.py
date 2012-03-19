#! /usr/bin/python 
# filename: 23.py

'''
Find the sum of all the positive integers which cannot be written as the 
sum of two abundant numbers.
number: perfect, deficient, abundant
'''
#global list to store the abundant number
ls = []

def divisors(n):
  '''store all the divisors in its specific list
  and return its sum'''
  return sum(list(i for i in xrange(1, n/2+1) if n%i==0))

def abundant(n):
  '''get all the abundant number below n 
  and make it a list'''
# abund = []
  for i in xrange(1,n):
    if i<divisors(i): ls.append(i)

#  return abund

def isAbundant(n):
  '''test if this given number n is abundant number or not
  if it is, return True, if not, return False'''
  for i in ls:
    temp = n - i
    if temp in ls: return True
    if i > n: break
  return False

def main():
  abundant(28123)
  total = sum(list(i for i in xrange(1, 28124)))
  abundantSum = 0

  for i in xrange(24, 28124):
    if isAbundant(i): 
      abundantSum += i
  print total-abundantSum


if __name__ == '__main__':
  main()

