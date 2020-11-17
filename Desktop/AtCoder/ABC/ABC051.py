#ABC051(A〜D) 全完

#A - Haiku

s = input()
print(s[:5] + " " + s[6:13] + " " + s[14:])

#B - Sum of Three Integers

k,s = map(int,input().split())
ans = 0
for x in range(k+1):
  for y in range(k+1):
    z = s-x-y
    if 0 <= z and z <= k:
      ans += 1
print(ans)

#C - Back and Forth

sx,sy,tx,ty = map(int,input().split())
a = tx-sx
b = ty-sy
#1周目
print('U' * b + 'R' * a + 'D' * b + 'L' * a, end="")
#2周目
print('L',end="")
print('U' * (b+1) + 'R' * (a+1) + 'DR' + 'D' * (b+1) + 'L' * (a+1),end="")
print('U')

#D - Candidates of No Shortest Paths

from scipy.sparse.csgraph import floyd_warshall

n,m = map(int,input().split())
matrix = [[0 for i in range(n)] for i in range(n)]
link_usage = [[1 for i in range(n)] for i in range(n)]
#隣接行列の作成
for i in range(m):
  a,b,c = map(int,input().split())
  matrix[a-1][b-1] = c
  matrix[b-1][a-1] = c

#ワーシャル・フロイト法（全点間最短距離，最短経路）
dist_matrix, predecessors = floyd_warshall(matrix, directed=False, return_predecessors=True)

#最短経路で用いるリンクを判別
for i in range(n):
  for j in range(n):
    while True:
      if predecessors[i][j] < 0:
        break
      link_usage[predecessors[i][j]][j] = 0
      j = predecessors[i][j]
      
count = 0
x = n*(n-1)//2-m
for i in range(n):
  for j in range(n):
    if link_usage[i][j] != 0:
      count += 1
print((count-n-2*x)//2)