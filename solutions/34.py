#! /usr/bin/python
# filename: 34.py

'''
Find the sum of all numbers which are equal to the sum of the factorial 
of their digits
This program is not that hard, just need to figure out the end num and 
remember to make temp as 0
'''
def factorial(n):
  if n == 1: return 1
  return n*factorial(n-1)

def main():
  dic = {0:1}
  end = 0
  temp = 0
  total = 0

  for i in xrange(1,10):
    dic[i] = factorial(i)
    end += dic[i]
  for i in xrange(10, end):
    for j in xrange(len(str(i))):
      temp += dic[int(str(i)[j])] 
    if temp == i: 
      total += temp
    temp = 0
  print total

if __name__ == '__main__':
  main()
