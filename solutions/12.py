#! /usr/bin/python
# filename: 12.py

# sequence of triangle numbers
import math

def triangleNum(n):
  temp = 0
  for i in range(1, n+1):
    temp += i
  return temp


def factorize(n):
  res = [1]
  #iterate over all even numbers first
  while n%2 == 0:
    res.append(2)
    n //= 2
  # try odd numbers up to sqrt(n)
  limit = math.sqrt(n+1)

  i = 3
  while i<limit:
    if n%i == 0:
      res.append(i)
      n //= i
      limit = math.sqrt(n+i)
    else:
      i += 2
  if n != 1:
    res.append(n)
  return res

def divsors(n):
  div = []
  factor = []
  factor = factorize(n)

  length = len(factor)
  for i in range(length-1):
    for j in range(i, length):
      temp = factor[i]*factor[j]
      if temp not in div:
        div.append(temp)

  return len(div)


def main():
  N = 100
  while True:
    num = triangleNum(N)
    temp = divsors(num) 
    if temp == 500:
      print num
      break
    else:
      N += 1




if __name__ == '__main__':
  main()

