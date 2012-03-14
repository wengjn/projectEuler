#! /usr/bin/python
# filename: 4.py

#brute force to solve the project euler 4
res = []

for x in range(100, 1000):
  for y in range(100, 1000):
    temp = x*y
    if str(temp) == str(temp)[::-1]:
      res.append(temp)

print max(res)
