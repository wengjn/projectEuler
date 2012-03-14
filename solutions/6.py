#! /usr/bin/python
# filename 6.py

# This is my solution to the problem 6

def main():
  sqSum = 0
  sumSq = 0
  total = 0

  for i in range(1, 101, 1):
    total += i
    sqSum += i*i

  sumSq = total * total
  print sumSq - sqSum


if __name__ =='__main__':
  main()

