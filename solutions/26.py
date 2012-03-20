#! /usr/bin/python
# filename: 26.py

'''
Find the value of d<1000 for which 1/d contains the longest recurring cycle
1/7=0.16666..., 0.1(6)
in Python, how do we get the decimal fraction part from division???
This one is hard!!!
Fermat's Little Theorem: a fraction 1/d has a cycle n if
(pow(10,n)-1)mod d = 0 for prime d
'''
def cycle_length(n):
  i = 1
  if n%2==0: return cycle_length(n/2)
  if n%5==0: return cycle_length(n/5)
  while True:
    if (pow(10, i)-1)%n==0: return i
    else: i += 1


def main():
  m = 0
  n = 0
  for d in xrange(1, 1000):
    c = cycle_length(d)
    if c > m:
      m = c
      n = d
  print n


if __name__ == '__main__':
  main()
