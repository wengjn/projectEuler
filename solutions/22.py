#! /usr/bin/python
# filename: 22.py

'''
What is the total of all the name scores in the file?
read from file, sort the list and then calculate the value of score
We could construct this string by for loop
first get the string full of alphbet 'abcd..xyz'
alpha = string.ascii_lowercase
'''
dic ={ 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, \
       'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, \
       'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, \
       'z':26 }

def getList():
  '''get the sorted list of names'''
  namels = []
  f = open('names.txt', 'r')
  text = f.read()
  namels = text.split(',')
  for i in range(len(namels)):
    namels[i]=namels[i][1:-1]
  return sorted(namels)

def getScore(str):
  '''get the score of each string'''
  str = str.lower()
  score = 0
  for i in range(len(str)):
    score += dic[str[i]]

  return score

def main():
  ls = []
  ls = getList()
  print ls[0], ls[1]
  total = 0
  for i in range(len(ls)):
    total += getScore(ls[i]) * (i+1)

  print total

if __name__ == '__main__':
  main()
