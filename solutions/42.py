#! /usr/bin/pythoon
# filename: 41.py

'''
How many triangle words does the list of common English words contain?
'''
dic ={ 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, \
        'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, \
        'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, \
        'z':26 }
def isTriangle(n):
  if n == 1: return True
  elif n == 2: return False
  i = 1
  while i <= (n/2+1):
    if 2 * n == i * (i + 1): return True
    i += 1
  return False

def wordValue(s):
  s = s.lower()
  value = 0
  for i in xrange(0, len(s)):
    value += dic[s[i]]
  return value

def main():
  # read words from file
  data = []
  filehandle = open('words.txt', 'r')
  a = filehandle.read()
  aa = a.split(',')
  for ai in aa:
    ai = ai.replace(r'"', '')
    data.append(ai)
  filehandle.close()

  # now, count all the triangle words
  count = 0
  for i in xrange(len(data)):
    if isTriangle(wordValue(data[i])):
      count += 1
  print count

if __name__ == '__main__':
  main()
