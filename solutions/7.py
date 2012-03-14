#! /usr/bin/python
# filename : 7.py

# find the 1001st prime number
# this is not a good program, it do the brute force algorithm
'''
import math

def main():
  primels = [2]

  i = 3
  j = 2
  while True:
#limit = int(math.sqrt(i+1))
    for j in range(2, i, 1):
      if i%j == 0: 
        break
    if j == (i-1):
      primels.append(i)
    i += 2
    if len(primels) == 10002:
      break
  
  print primels[10000]
  print primels[5]

if __name__ == '__main__':
  main()
'''

import time
import math

s = time.time()
def isPrime(n):
  if n == 2:
    return True
  elif n%2 == 0:
    return False

  for i in range(3, int((math.sqrt(n)+1))):
    if n%i == 0:
      return False
    i += 1

  return True

N, T = 1, 3
while N<10001:
  if isPrime(T):
    N += 1
  T += 2

print T-2
print time.time()-s 
