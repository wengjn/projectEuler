#! /usr/bin/python
# filename: 76.py

'''
how many different ways can one hundred be written as a sum of positive 
integers, at least 2
this problem is like coin changing problem31
dynamic programming
need to look it more carefully from this on
'''


def main():

  target = 100
  ns = range(1, 100)
  ways = [1] + [0]*target

  for n in ns:
    for i in range(n, target+1):
      ways[i] += ways[i-n]

  print ways[target]


if __name__ == '__main__':
  main()
