#! /usr/bin/python
# filename: 39.py

'''
If p is the perimeter of a right angle triangle {a,b,c},which value
for p<=1000, has the most solutions?
interesting: a+b+c=p and a**2+b**2=c**2
'''

def main():
  t_max=0
  p_limit = 1000
  for p in range(p_limit/2, p_limit+1, 2):
    t = 0
    for a in range(2, p/4+1):
      if p*(p-2*a)%(2*(p-a))==0: t+=1
      if t> t_max: (t_max, p_max) = (t,p)

  print p_max

if __name__ == '__main__':
  main()
