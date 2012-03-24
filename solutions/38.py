#! /usr/bin/python
# filename: 38.py

'''
What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with(1,2..n) where n>1
starting with n=2
9?*1++9?*2 and 9??*1+9??*2 they will never yield a 9digit number
but 9???*1+9???*2 will, so our starting search must be a 4 digit number 
beginnning with 9 and never contain 0
it should be obvious that any n>2 is impossible
'''
def isPandigital(n, s=9):
  n = str(n)
  return len(n)==s and not '1234567890'[:s].strip(n)

def main():
  for i in range(9876, 9123, -1):
    p = str(i*1)+ str(i*2)
    if isPandigital(int(p)):
      print p
      break

if __name__ == '__main__':
  main()
