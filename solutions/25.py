#! /usr/bin/python
# filename: 25.py

'''
What is the first term in the Fibonacci sequence to contain 1000 digits
Fibonacci sequence
This one may run really really slow. Still needs more thought on that!!
another good way is:
nm =1
n=1
count =2
while len(str(n))<1000:
  (n,nm)=n+nm, n
  count += 1
print count
'''

def fib(n):
  if n == 1: return 1
  if n == 2: return 1
  if n > 2:
    return fib(n-1) + fib(n-2)

def main():
  i = 12
  while True:
    temp = fib(i)
    if len(str(temp))==1000:
      print temp
      break
    else:
      i += 1

if __name__ == '__main__':
  main()
