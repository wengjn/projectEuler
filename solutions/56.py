#! /usr/bin/python
# filename: 56.py

'''
the sum of the digits in each number
what is the maximum digital sum
'''

def calc(a, b):
  '''compute the value of a^b'''
  res = a
  for i in range(1, b):
    res = res * a

  return res

def getSum(n):
  '''compute the digital sum of this number n'''
  s = str(n)
  res = 0
  for i in range(len(s)):
    res += int(s[i])

  return res

def main():
  larger = 0
  temp = 0
  digSum = 0
  for i in range(2, 100):
    for j in range(2, 100):
      temp = calc(i, j)
      digSum = getSum(temp)
      if digSum > larger:
        larger = digSum

  print larger


if __name__ == '__main__':
  main()
