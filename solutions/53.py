#! /usr/bin/python
# filename: 53.py

'''
combination
How many, values of nCr, are greater than one-million
'''
def factorial(n):
  '''compute the value of n! '''
  res = 1
  for i in range(1, n+1):
    res = res * i

  return res

def calc(n, r):
  '''calculate nCr, the combination'''
  return factorial(n) / (factorial(r) * factorial(n-r))


def main():
  total = 0
  for i in range(1, 101):
    for j in range(1, i):
      if calc(i, j) > 1000000:
        total += 1

  print total

if __name__ == '__main__':
  main()
