#! /usr/bin/python
# filename: 16.py

# python is really powerful

def main():
  summ = 0
  text = str(2**1000)

  for i in range(len(text)):
    summ += int(text[i])


  print summ


if __name__=='__main__':
  main()
