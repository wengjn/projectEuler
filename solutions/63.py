#! /usr/bin/python
# filename: 63.py

'''
how many n-digit positive integers exist which are also an nth power
one way to know how many digits a number has is to use formula:
int(log10(n)) + 1
'''
from math import log10

def main():
  s = 0
  for n in range(1, 10):
    s += int(1/(1-log10(n)))

  print s


if __name__ == '__main__':
  main()
