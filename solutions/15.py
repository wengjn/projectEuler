#! /usr/bin/python
# filename: 15.py

'''
00 01 02
10 11 12
20 21 22
'''
#everytime, just add by one
#compute the routes needed to get to the bottom right from upper left
#so how to solve this:
'''
Each movement in the horizontal is a zero.
Each movement in the vertical is a one.
1st binary# in this series:
0000000000000000000011111111111111111111
1111111111111111111100000000000000000000
For the numbers in between, the amount of zeros should be the same as ones, In other words, the ones and zeros have to be rearranged. This is a problem of permutation and combination.
So, the total should be: 40!/(20!)(20!)

'''

def fac(n):
  if n == 0:
    return 1
  else:
    return n*fac(n-1)

def main():
  rows, cols = 20, 20
  print fac(rows+cols) /(fac(rows)*fac(cols))



if __name__ == '__main__':
  main()
