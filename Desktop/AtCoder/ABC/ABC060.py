#ABC060(A〜D) A,B,C 完

#A - Shiritori

a,b,c = map(str,input().split())
if a[-1] == b[0] and b[-1] == c[0]:
  print('YES')
else:
  print('NO')

#B - Choose Integers

a,b,c = map(int,input().split())
line = []
for i in range(1,b+1):
  line.append(a*i % b)
if c in line:
  print('YES')
else:
  print('NO')

#C - Sentou

n,t = map(int,input().split())
T_list = list(map(int,input().split()))
ans = 0
for i in range(n-1):
  ans += min(T_list[i+1]-T_list[i],t)
print(ans + t)