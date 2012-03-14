#! /usr/bin/python
# filename: 14.py

# this is not my program, cp from johnnycoder.com
# hard!!!
# sequence end to 1

def collatz_length(n):
  # 0 and 1 return itself as length
  if n<=1: return n

  length = 1
  while(n!=1):
    if(n%2==0):
      n/=2
    else:
      n = 3*n + 1
    length += 1

  return length

startingnum, longest_chain = 1, 0
for x in xrange(1, 1000001):
  l = collatz_length(x)
  if l > longest_chain: startingnum, longest_chain = x, l

print startingnum
print longest_chain

