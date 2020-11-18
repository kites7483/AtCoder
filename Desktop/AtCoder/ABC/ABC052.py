#ABC052(A〜D) 全完

#A - Two Rectangles

a,b,c,d = map(int,input().split())
print(max(a*b,c*d))

#B - Increment Decrement

n = int(input())
s = input()
ans = 0
x = 0
for i in s:
  if i == 'I':
    x += 1
  else:
    x -= 1
  if x > ans:
    ans = x
print(ans)

#C - Factors of Factorial

import math

def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr
  
n = int(input())
ans = 1
mod = 10**9+7
line = [0 for i in range(1001)]
if  n == 1:
  print(ans)
else:
  for i in range(2,n+1):
    primes = factorization(i)
    for prime in primes:
      line[prime[0]] += prime[1]
      
  for i in line:
    if i > 0:
      ans *= (i+1)
    ans %= mod
  print(ans)

#D - Walk and Teleport

n,a,b = map(int,input().split())
line = list(map(int,input().split()))
ans = 0
for i in range(n-1):
  x = line[i+1] - line[i]
  ans += min(a*x,b)
print(ans)