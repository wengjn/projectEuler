#! /usr/bin/python
# filename: 13.py

# this is to compute the first 10 digit number of the sum, a big sum

def main():
  try:
    f = open('data13.txt', 'r')
  except IOError:
    print 'cannot open data13.txt'

  text = f.readlines()
  f.close()
  summ = 0
  for i in range(100):
    temp = text[i].strip()
    summ += int(temp)

  print str(summ)[0:10]

if __name__ == '__main__':
  main()
