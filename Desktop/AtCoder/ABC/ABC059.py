#ABC059(A〜D) A,B,C 完

#A - Three-letter acronym

a,b,c = map(str, input().split())
print(a[0].upper() + b[0].upper() + c[0].upper())

#B - Comparison

a = int(input())
b = int(input())
if a > b:
  print('GREATER')
elif a < b:
  print('LESS')
else:
  print('EQUAL')

#C - Sequence

n = int(input())
line = list(map(int,input().split()))
_sum = 0
ans1 = 0
ans2 = 0
for i in range(n):
  _sum += line[i]
  if i % 2 == 0:
    if _sum >= 0:
      ans1 += (_sum + 1)
      _sum = -1
  else:
    if _sum <= 0:
      ans1 += (1 - _sum)
      _sum = 1
       
_sum = 0

for i in range(n):
  _sum += line[i]
  if i % 2 == 0:
    if _sum <= 0:
      ans2 += (1 - _sum)
      _sum = 1
  else:
    if _sum >= 0:
      ans2 += (_sum + 1)
      _sum = -1
        
print(min(ans1,ans2))