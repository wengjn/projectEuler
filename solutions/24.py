#! /usr/bin/python
# filename: 24.py

'''
what is the mmillionth lexicographic permutation of the digits 0...9
The big problem here is how to get the permutation of 0..9
10 for loop?? no
took a little help from projecteuler.net/thread=24
'''
def fact(n):
  f = 1
  for x in xrange(1, n+1): f=f*x
  return f

def permutation(orig_nums, n):
  nums = list(orig_nums)
  perm = []
  while len(nums):
    divider = fact(len(nums)-1)
    pos = n/divider
    n = n%divider
    perm.append(nums[pos])
    nums = nums[0:pos] + nums[pos+1:]
  return perm

def main():
  print ''.join(str(x) for x in permutation(range(0,10), 999999))

if __name__=='__main__':
  main()
