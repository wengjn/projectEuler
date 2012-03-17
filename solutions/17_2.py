#! /usr/bin/python
# filename: 17_2.py

# this one is reference to johnnycoder.com

def to_word(n):
  h = { 1:'one', 2:'two', 3:'three', 4:'four', 5:'five', 6:'six', \
        7:'seven', 8:'eight', 9:'nine', 10:'ten', 11:'eleven', \
        12:'twelve', 13:'thirteen', 14:'fourteen', 15:'fifteen',\
        16:'sixteen', 17:'seventeen', 18:'eighteen', 19:'nineteen',\
        20:'twenty', 30:'thirty', 40:'forty', 50:'fifty', 60:'sixty',\
        70:'seventy', 80:'eighty', 90:'ninety', 100:'hundred', \
        1000:'thousand' }

  word = ''

  # reverse the positions so that can be easy determine its ones, tens
  # hundreds ...
  a = [int(x) for x in str(n)[::-1]]

  # thousands position
  if len(a) == 4 and a[3] != 0:
    word = h[a[3]] + ' thousand '

  # hundreds position
  if len(a) >= 3 and a[2] != 0:
    word += h[a[2]] + ' hundred'
    if len(a) >= 2 and a[1] != 0:
      word += ' and'
    elif len(a) >= 1 and a[0] != 0:
      word += ' and'

  # tens and ones position
  tens_position_value = 99
  if len(a) >= 2 and a[1] != 0:
    tens_position_value = int(a[1]) * 10 + a[0]

    if tens_position_value <= 20:
      word += ' ' + h[tens_position_value]
    else:
      word += ' ' + h[(a[1]*10)]

  if len(a) >= 1 and a[0] != 0 and tens_position_value > 20:
    word += ' ' + h[a[0]]

  return word.replace(' ', '')

def to_word_length(n):
  return len(to_word(n))

def main():
  print sum([to_word_length(i) for i in xrange(1, 1001)])

if __name__ == '__main__':
  main()




