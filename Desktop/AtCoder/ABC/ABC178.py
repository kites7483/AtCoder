#A - Not

x = int(input())
if x == 1:
  print(0)
else:
  print(1)

#B - Product Max

a,b,c,d = map(int, input().split())
print(max(a*c,a*d,b*c,b*d))

#C - Ubiquity

n = int(input())
if n == 1:
  print(0)
else:
  x = 10**9 + 7
  a = (-1) * (10**n - 8**n - 2 * (10**n - 9**n))
  print(a%x)

#D - Redistribution

import itertools
from operator import mul
from functools import reduce

def combinations_count(n, r):
    r = min(r, n - r)
    numer = reduce(mul, range(n, n - r, -1), 1)
    denom = reduce(mul, range(1, r + 1), 1)
    return numer // denom

s = int(input())
if s == 1 or s == 2:
  print(0)
elif s >= 3 and s <= 5:
  print(1)
else:
  ans = 1
  for i in range(2,1000):
    x = s - 3*i
    if x < 0:
      break
    ans += combinations_count(x + i - 1, x)
  print(ans % (10**9 + 7))

#E - Dist Max

n = int(input())
x = []
y = []
z = []
for i in range(n):
  a,b = map(int, input().split())
  x.append(a+b)
  y.append(a-b)
  z.append(b-a)
print(max(max(x) - min(x),max(y) - min(y),max(z) - min(z)))