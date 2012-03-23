#! /usr/bin/python
# filename: 36.py

'''
Find the sum of all numbers less than one million, which are palindromic
in base 10 and base 2
the key is to convert from decimal into binary
'''

def decimal2binary(n):
  '''convert decimal integer n to binary string bStr'''
  bStr = ''
  if n<0:
     raise ValueError, 'must be a positive integer'
  if n==0:
     return '0'
  while n>0:
    bStr += str(n%2)
    # n = n/2
    n = n >> 1
  return bStr
  
def isPalindromic(n):
  if str(n) == str(n)[::-1]:
    return True
  else:
    return False

def main():
  total,count = 0,0
  for i in xrange(1, 1000000):
    if isPalindromic(i) and isPalindromic(decimal2binary(i)):
        count += 1
        total += i

  print 'count:',count
  print 'total:',total

if __name__ == '__main__':
  main()
