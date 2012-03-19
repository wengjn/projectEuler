#! /usr/bin/python
# filename: 21.py

'''
Evaluate the sum of all the amicable numbers under 10000
d(a) = b, d(b) = a, a and b are called amicable numbers.
'''
def divisors(n):
  ''' store all the divisors in its specific list'''
  return list(i for i in xrange(1, n/2+1) if n%i == 0)


def main():
  '''make a dictionary to store the divisors of all the numbers
  '''
  pair = dict(((n, sum(divisors(n))) for n in xrange(1, 10000)))
  print sum(n for n in xrange(1, 10000) if pair.get(pair[n], 0) == n and pair[n] != n)


if __name__ == '__main__':
  main()
