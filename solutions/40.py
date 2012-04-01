#! /usr/bin/python
# filename: 40.py

'''
Finding the nth digit of the fractional part of the irrational number
'''

def main():
  temp = ''
  for i in xrange(1, 1000000):
    temp += str(i)

  print int(temp[0]) * int(temp[9]) * int(temp[99]) * int(temp[999]) \
        * int(temp[9999]) * int(temp[99999]) * int(temp[999999])

if __name__ == '__main__':
  main()
