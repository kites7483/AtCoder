#ABC055(A〜D) A,B,C 完

#A - Restaurant

n = int(input())
print(800*n - (n//15)*200)

#B - Training Camp

n = int(input())
ans = 1
for i in range(1,n+1):
  ans *= i
  ans %= 10**9+7
print(ans)

#C - Scc Puzzle

n,m = map(int,input().split())
if 2*n >= m:
  print(m//2)
else:
  m -= 2*n
  print(n + m//4)