#! /usr/bin/python
# filename: 16.py

# python is really powerful

# there is also one line method
'''
reduce(lambda x, y: x + y, [int(i) for i in str(2**1000)])
sum(int(digit) for digit in str(2**1000))
'''

def main():
  summ = 0
  text = str(2**1000)

  for i in range(len(text)):
    summ += int(text[i])


  print summ


if __name__=='__main__':
  main()
