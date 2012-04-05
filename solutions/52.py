#! /usr/bin/python
# filename: 52.py

'''
Find the smallest positive integer, x such that 2x,3x,4x,5x,6x
contain the same digits
'''

def containSame(n1, n2):
  s1 = str(n1)
  s2 = str(n2)

  if len(s1) != len(s2): return False
  for i in s1:
    if i not in s2: return False
  return True

def main():
  i = 102
  while True:
    if containSame(i, 2*i) and containSame(3*i, 4*i) and \
        containSame(5*i, 6*i) and containSame(i, 3*i) and \
         containSame(i, 5*i):
      print i
      break
    i += 1


if __name__ == '__main__':
  main()
