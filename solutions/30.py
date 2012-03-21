#! /usr/bin/python
# filename: 29.py

'''
Find the sum of all the numbers that can be written as the sum of fifth
powers of their digits
numbers could be 3/4/5/6 digits
other method:
m = {str(x): x**5 for x in xrange(10)}
print sum(i for i in xrange(2,1000000) if sum(m[x] for x in str(i))==i)
somebody do it with only one line:
sum(filter(lambda x: x-sum(int(i)**5 for i in str(x))==0, range(2, 5*(9**5))))
'''

def main():
  dic = {}
  for i in xrange(0, 10):
    dic[i] = i**5

  total = 0
  temp = 0
  for i in xrange(100000, 1000000):
    for j in xrange(0, 6):
      temp += dic[int(str(i)[j])]
    if temp == i: 
      total += temp
      print i
    temp = 0
  print total

if __name__=='__main__':
  main()
