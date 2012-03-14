#! /usr/bin/python
# filename: 5.py

# project euler 5

# at first solve this problem only by pen and paper
#method 1
'''
i = 1
for k in range(1, 21):
  if i%k>0:
    for j in range(1, 21):
      if (i*j) % k == 0:
        i = i*j
        break

print i
'''
#method 2
import time

s = time.time()

def gcd(a, b):
  while b != 0:
    a, b = b, a%b
    return a

def lcm(a, b):
  return a*b/gcd(a,b)

print reduce(lcm, range(1, 20+1))
print "time: %d" % (time.time() -s)
