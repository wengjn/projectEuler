#! /usr/bin/python
# filename: 9.py

# find pythagorean 

def findabc():
  a, b, c = 2, 2, 3
 
  for a in range(1,1000):
    for b in range(a, 1000):
      c = 1000 - a - b
      temp = a*a + b*b
      if temp == c*c:
        return a*b*c

def main():
  print findabc()

if __name__ == '__main__':
  main()
