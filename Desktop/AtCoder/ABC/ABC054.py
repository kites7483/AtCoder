#ABC054(A〜D) A,B,C 完

#A - One Card Poker

a,b = map(int,input().split())
if a == b:
  print('Draw')
else:
  if a == 1:
    print('Alice')
  elif b == 1:
    print('Bob')
  else:
    if a > b:
      print('Alice')
    else:
      print('Bob')

#B - Template Matching

n,m = map(int,input().split())
x = n-m+1
n_list = []
m_list = []
for i in range(n):
  n_list.append(input())
for i in range(m):
  m_list.append(input())

for i in range(x):
  for j in range(x):
    count = 0
    for k in range(m):
      if m_list[k] == n_list[i+k][j:j+m]:
        count += 1
    if count == m:
      print('Yes')
      exit()
print('No')

#C - One-stroke Path

import itertools

n,m = map(int, input().split())
matrix = [[0 for i in range(n)] for i in range(n)]
nodes = [i for i in range(n)]
ans = 0
for i in range(m):
  a,b = map(int,input().split())
  matrix[a-1][b-1] = 1
  matrix[b-1][a-1] = 1

for order in itertools.permutations(nodes,n):
  count = 0
  if order[0] != 0:
    continue
  for i in range(n-1):
    if matrix[order[i]][order[i+1]] == 1:
      count += 1
  if count == n-1:
    ans += 1
print(ans)