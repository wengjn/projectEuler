#! /usr/bin/python
# filename: 38.py

'''
What is the largest 1 to 9 pandigital 9-digit number that can be formed
as the concatenated product of an integer with(1,2..n) where n>1
'''
def isPandigital(n, s=9):
  n = str(n)
  return len(n)==s and not '1234567890'[:s].strip(n)

def main():
  for i in range(1000000000, 918273644, -1):
    if isPandigital(i):
     # 

if __name__ == '__main__':
  main()
