#A - twiblr

a,b = map(int,input().split())
print(2*a+100-b)

#B - Almost GCD

n = int(input())
line = list(map(int, input().split()))
ans = 0
max_count = 0
for i in range(2,1001):
  count = 0
  for j in line:
    if j % i == 0:
      count += 1
  if count > max_count:
    max_count = count
    ans = i
print(ans)

#C - To 3

s = input()
if int(s) % 3 == 0:
  print(0)

else:
  count = 0
  line = [0 for i in range(3)]
  for i in s:
    count += int(i)
    line[int(i)%3] += 1

  if count < 3:
    print(-1)
    exit()

  if count % 3 == 1:
    if line[1] >= 1 and len(s) >= 2:
      print(1)
    elif line[2] >= 2 and len(s) >= 3:
      print(2)
    else:
      print(-1)
    exit()

  if count % 3 == 2:
    if line[2] >= 1 and len(s) >= 2:
      print(1)
    elif line[1] >= 2 and len(s) >= 3:
      print(2)
    else:
      print(-1)
    exit()

#D - Wandering

n = int(input())
line = list(map(int, input().split()))
ans = 0
for i in range(n-1):
  line[i+1] += line[i]
point = 0
positive_max = 0
point_list = [0]
for i in range(n):
  if line[i] > positive_max:
    positive_max = line[i]
  point_list.append(point + positive_max)
  point += line[i]
print(max(point_list))

#E - Akari (pypy3)

import copy
import itertools

h,w,n,m = map(int, input().split())
matrix = [[0 for i in range(w)] for i in range(h)]
light_list = []
for i in range(n):
  line = list(map(int, input().split()))
  light_list.append(line)
for i in range(m):
  line = list(map(int, input().split()))
  matrix[line[0]-1][line[1]-1] = -1
  
matrix_copy = copy.deepcopy(matrix)

#横方向
for point in light_list:
  a,b = point[0],point[1]
  if matrix[a-1][b-1] == 0:
    matrix[a-1][b-1] = 1
    #右方向
    while b < w:
      if matrix[a-1][b] != -1:
        matrix[a-1][b] = 1
        b += 1
      else:
        break
    #左方向
    while b > 1:
      if matrix[a-1][b-2] != -1:
        matrix[a-1][b-2] = 1
        b -= 1
      else:
        break

#縦方向
for point in light_list:
  a,b = point[0],point[1]
  if matrix_copy[a-1][b-1] == 0:
    matrix_copy[a-1][b-1] = 1
    #下方向
    while a < h:
      if matrix_copy[a][b-1] != -1:
        matrix_copy[a][b-1] = 1
        a += 1
      else:
        break
    #上方向
    while a > 1:
      if matrix_copy[a-2][b-1] != -1:
        matrix_copy[a-2][b-1] = 1
        a -= 1
      else:
        break

matrix_add = list(map(lambda x,y: list(map(lambda a,b: a+b, x,y)), matrix, matrix_copy))
matrix_flat = list(itertools.chain.from_iterable(matrix_add))
print(sum(x>0 for x in matrix_flat))