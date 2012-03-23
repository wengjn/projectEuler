#! /usr/bin/python
# filename: 31.py

'''
Coin Change problem
How many different ways can 200p(L2) be mad using any numbers of coins?
1p,2p,5p,10p,20p,50p,100p,200p
at first, I was thinking of 7 loops to solve this problem, turns out quite
slow.
use dynamic programming, typical use of partitions
'''

def main():
  target = 200
  coins = [1, 2,5, 10, 20, 50, 100, 200]
  ways = [1]+[0]*target

  for coin in coins:
    for i in xrange(coin, target+1):
      ways[i] += ways[i-coin]
  print ways[target]

if __name__=='__main__':
  main()
