#! /usr/bin/python
# filename: 85.py

'''
find the area of the grid with the nearest solution
note this funny math
the sum of counting number (1..x) multiplied by the sum of counting number 
(1..y), x = 3, y = 2, (9+3)(4+2)/4 = 18
(x^2 + x)(y^2 + y) / 4
'''

def main():
  maxnum = 2000000 
  near = 100000
  result = 0
  for i in range(2,100):
    for j in range(2, 100):
      count = (i*i + i)*(j*j + j)/4
      diff = maxnum - count
      if abs(diff) < near:
        near = abs(diff)
        result = i * j

  print result


if __name__ == '__main__':
  main()
