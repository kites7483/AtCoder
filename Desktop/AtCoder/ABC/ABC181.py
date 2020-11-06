# A - Heavy Rotation

n = int(input())
if n % 2 == 0:
  print('White')
else:
  print('Black')

# B - Trapezoid Sum

n = int(input())
ans = 0
for i in range(n):
  a,b = map(int,input().split())
  x = (b-a+1)*(b-a+2)//2 + (a-1)*(b-a+1)
  ans += x
print(ans)

# C - Collinearity

import itertools

n = int(input())
ans = 'No'
a = []
for i in range(n):
  line = list(map(int, input().split()))
  a.append(line)

numbers = [i for i in range(n)]
for v in itertools.combinations(numbers,3):
  if abs((a[v[0]][0]-a[v[2]][0])*(a[v[1]][1]-a[v[2]][1])-(a[v[1]][0]-a[v[2]][0])*(a[v[0]][1]-a[v[2]][1])) == 0:
    ans = 'Yes'
    break
print(ans)

# D - Hachi (ゴリ押し)

s = int(input())
ans = 'No'
if len(str(s)) == 1:
  if s == 8:
    print('Yes')
  else:
    print('No')
elif len(str(s)) == 2:
  if s == 16 or s == 61 or s == 24 or s == 42 or s == 32 or s == 23 or s == 48 or s == 84 or s == 56 or s == 65 or s == 64 or s == 46 or s == 72 or s == 27 or s == 88 or s == 96 or s == 69:
    print('Yes')
  else:
    print('No')
else:
  s = str(s)
  a = [0 for i in range(10)]
  for i in s:
    a[int(i)] += 1
    
  if a[4] >= 1 and a[8] >= 1:
    ans = 'Yes'
  if a[1] >= 1 and a[2] >= 1:
    a[1] -= 1
    a[2] -= 1
    if a[1] >= 1 or a[3] >= 1 or a[5] >= 1 or a[7] >= 1 or a[9] >= 1:
      ans = 'Yes'
    a[1] += 1
    a[2] += 1
  if a[2] >= 1 and a[8] >= 1:
    a[2] -= 1
    a[8] -= 1
    if a[1] >= 1 or a[3] >= 1 or a[5] >= 1 or a[7] >= 1 or a[9] >= 1:
      ans = 'Yes'
    a[2] += 1
    a[8] += 1
  if a[3] >= 1 and a[6] >= 1:
    a[3] -= 1
    a[6] -= 1
    if a[1] >= 1 or a[3] >= 1 or a[5] >= 1 or a[7] >= 1 or a[9] >= 1:
      ans = 'Yes'
    a[3] += 1
    a[6] += 1
  if a[4] >= 2:
    a[4] -= 2
    if a[1] >= 1 or a[3] >= 1 or a[5] >= 1 or a[7] >= 1 or a[9] >= 1:
      ans = 'Yes'
    a[4] += 2
  if a[5] >= 1 and a[2] >= 1:
    a[5] -= 1
    a[2] -= 1
    if a[1] >= 1 or a[3] >= 1 or a[5] >= 1 or a[7] >= 1 or a[9] >= 1:
      ans = 'Yes'
    a[5] += 1
    a[2] += 1
  if a[6] >= 1 and a[8] >= 1:
    a[6] -= 1
    a[8] -= 1
    if a[1] >= 1 or a[3] >= 1 or a[5] >= 1 or a[7] >= 1 or a[9] >= 1:
      ans = 'Yes'
    a[6] += 1
    a[8] += 1
  if a[7] >= 1 and a[6] >= 1:
    a[7] -= 1
    a[6] -= 1
    if a[1] >= 1 or a[3] >= 1 or a[5] >= 1 or a[7] >= 1 or a[9] >= 1:
      ans = 'Yes'
    a[7] += 1
    a[6] += 1
  if a[9] >= 1 and a[2] >= 1:
    a[9] -= 1
    a[2] -= 1
    if a[1] >= 1 or a[3] >= 1 or a[5] >= 1 or a[7] >= 1 or a[9] >= 1:
      ans = 'Yes'
    a[9] += 1
    a[2] += 1
    
  if a[1] >= 1 and a[6] >= 1:
    a[1] -= 1
    a[6] -= 1
    if a[2] >= 1 or a[4] >= 1 or a[6] >= 1 or a[8] >= 1:
      ans = 'Yes'
    a[1] += 1
    a[6] += 1
  if a[2] >= 1 and a[4] >= 1:
    a[2] -= 1
    a[4] -= 1
    if a[2] >= 1 or a[4] >= 1 or a[6] >= 1 or a[8] >= 1:
      ans = 'Yes'
    a[2] += 1
    a[4] += 1
  if a[3] >= 1 and a[2] >= 1:
    a[3] -= 1
    a[2] -= 1
    if a[2] >= 1 or a[4] >= 1 or a[6] >= 1 or a[8] >= 1:
      ans = 'Yes'
    a[3] += 1
    a[2] += 1
  if a[5] >= 1 and a[6] >= 1:
    a[5] -= 1
    a[6] -= 1
    if a[2] >= 1 or a[4] >= 1 or a[6] >= 1 or a[8] >= 1:
      ans = 'Yes'
    a[5] += 1
    a[6] += 1
  if a[4] >= 1 and a[6] >= 1:
    a[4] -= 1
    a[6] -= 1
    if a[2] >= 1 or a[4] >= 1 or a[6] >= 1 or a[8] >= 1:
      ans = 'Yes'
    a[4] += 1
    a[6] += 1
  if a[2] >= 1 and a[7] >= 1:
    a[2] -= 1
    a[7] -= 1
    if a[2] >= 1 or a[4] >= 1 or a[6] >= 1 or a[8] >= 1:
      ans = 'Yes'
    a[2] += 1
    a[7] += 1
  if a[8] >= 2:
    a[8] -= 2
    if a[2] >= 1 or a[4] >= 1 or a[6] >= 1 or a[8] >= 1:
      ans = 'Yes'
    a[8] += 2
  if a[6] >= 1 and a[9] >= 1:
    a[6] -= 1
    a[9] -= 1
    if a[2] >= 1 or a[4] >= 1 or a[6] >= 1 or a[8] >= 1:
      ans = 'Yes'
    a[6] += 1
    a[9] += 1
  print(ans)