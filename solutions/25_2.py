#! /usr/bin/python
# filename: 25_2.py

'''
first 1000 digit of fib sequence
ref from web
Saying that a number contains 1000 digits is the same as saying that it's greater than 10**999. The nth Fibonacci number is [phi**n / sqrt(5)], where the brackets denote "nearest integer". So we need phi**n/sqrt(5) > 10**999 n * log(phi) - log(5)/2 > 999 * log(10) n * log(phi) > 999 * log(10) + log(5)/2 n > (999 * log(10) + log(5) / 2) / log(phi) A handheld calculator shows the right hand side to be 4781.8593, so 4782 is the first integer n with the desired property. Why bother with a computer on this one?
'''

import math
phi = (1+pow(5, 0.5))/2
c=math.log10(5)/2
logphi = math.log10(phi)
n=1
while True:
  if n*logphi-c>=999:
    print n
    break
  n += 1
