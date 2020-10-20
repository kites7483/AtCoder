#A - box

n,a,b = map(int,input().split())
print(n - a + b)

#B - Various distances

import numpy as np

n = int(input())
line = list(map(int,input().split()))
m = 0
l = 0
k = 0
for i in line:
  a = abs(i)
  m += a
  l += a**2
  if k < a:
    k = a
print(m)
print(np.sqrt(l))
print(k)

#C - Cream puff

#約数の列挙
def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
line = make_divisors(n)
for i in line:
  print(i)

#D - Takahashi Unevolved

x,y,a,b = map(int,input().split())
ans = 0
while b > x*(a-1):
  if x*a < y:
    x *= a
    ans += 1
  else:
    break
ans += ((y-x-1)//b)
print(ans)