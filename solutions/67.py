#! /usr/bin/python
# filename: 67.py

'''
Find the maximum total from top to bottom in triangle.txt
You cannot brute force this one, since it will have 2**99 ways
Find out an efficient algorithm to solve it

while I'm writing this code, I found I forgot how to read from files
'''

def main():
  data =[]
  f = open('triangle.txt', 'r')
  triangle = f.read()
  for line in triangle:
    data.append([line])
  f.close()

  for i in xrange(4):
    print data[i]

if __name__ == '__main__':
  main()
