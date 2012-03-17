#! /usr/bin/python
# filename: 17.py

# how many letters would be used in the numbers
# first time use dictionary here!!!
# at first, I was wrong at 100 position, forget to count 100 into if..else
# statement
# now it is working

dic = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six',
         7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', 
          12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',
          16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',
          20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',
          70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred',
          1000:'onethousand' }

def countNum(n):
  word = ''
  ge, shi, bai, left = 0, 0, 0, 0
  # construct words and then add it into dictionary
  # two numbers
  if n>20 and n<100 and n not in dic.keys():
    shi = int(str(n)[0])*10
    ge = int(str(n)[1])
    word = dic[shi] + dic[ge]
    dic[n] = word
  elif n>=100 and n<1000:
    bai = int(str(n)[0])
    left = int(str(n)[1:])
    if left:
      word = dic[bai] + 'hundredand' + dic[left]
    else:
      word = dic[bai] + 'hundred'
    dic[n] = word

  
  return len(dic[n])

def main():
  total = 0
  print countNum(100)
  for i in range(1,1001):
    total += countNum(i)
  print total

if __name__=='__main__':
  main()
