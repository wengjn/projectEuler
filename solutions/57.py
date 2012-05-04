#! /usr/bin/python
#! filename: 57.py

'''
how many fractions contain a numberator with more digits than denominator
compute with the num/denom, fraction
n(k+1) = n(k) + 2*d(k)
d(k+1) = n(k) + d(k)  -> d(k+1) = n(k+1) - d(k)
'''


def main():
  n = 3
  d = 2
  result = 0
  for i in range(1000):
    n = n + 2 * d
    d = n - d
    if len(str(n)) > len(str(d)): result += 1

  print result

if __name__ == '__main__':
  main()
