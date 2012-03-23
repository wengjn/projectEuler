#! /usr/bin/python
# filename: 33.py

'''
Discover all the fractions with an unorthodox cancelling method
'''

def main():
  product = 1
  for i in xrange(1,10):
    for j in xrange(1,10):
      for k in xrange(1,10):
        num1 = int(str(j)+str(i))
        den1 = int(str(i)+str(k))
        if num1*k==den1*j and j != k:
          product = product * k
          print j,i,k
  print product

if __name__ == '__main__':
  main()
