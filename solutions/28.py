#! /usr/bin/python
# filename: 28.py

'''
what is the sum of the numbers on the diagonals in a 1001 by 1001 spiral 
formed in the same way?
21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13
sum = 21+7+1+3+13 + 17+5+9+25
we can also only use one line to get this:
sum(4*n**2-6*n+6 for n in xrange(3, 1002, 2))+1

'''
def diag(n):
  '''return a list with four diagonal numbers with n by spiral'''
  ls = []
  ls.append(n*n)
  ls.append(ls[0] - n + 1)
  ls.append(ls[1] - n + 1)
  ls.append(ls[2] - n + 1)
  return ls

def main():
  total = 0
  for i in xrange(3, 1003, 2):
    total += sum(diag(i))

  print total+1

if __name__ == '__main__':
  main()

