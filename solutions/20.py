#! /usr/bin/python
# filename: 20.py

# factorial

print reduce(lambda x, y: x+y, [int(i) for i in str(reduce(lambda x,y: x*y, range(1, 100)))])
