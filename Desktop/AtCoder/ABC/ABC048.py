#ABC048(A〜D) A,B,C 完

#A - AtCoder *** Contest

a,b,c = map(str, input().split())
print('A' + b[0] + 'C')

#B - Between a and b ...

a,b,x = map(int,input().split())
c = b//x + 1
if a == 0:
  d = 0
else:
  d = (a-1)//x + 1
print(c-d)

#C - Boxes and Candies

n,x = map(int,input().split())
line = list(map(int, input().split()))
ans = 0
for i in range(n-1):
  if line[i] >= x:
    ans += (line[i]-x) + line[i+1]
    line[i] = x
    line[i+1] = 0
  elif line[i] + line[i+1] >= x:
    ans += line[i]+line[i+1]-x
    line[i+1] = x - line[i]
  else:
    continue
print(ans)