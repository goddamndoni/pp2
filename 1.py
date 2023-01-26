from math import prod
from random import randrange

a = int(input())
d = int(input())
l = [0]*a
for i in range(a):
    l[i] = a*pow(d,i)
print(l)
#pp2 best course
