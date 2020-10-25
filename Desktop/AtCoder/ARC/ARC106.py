#A - 106

n = int(input())
count = 0
for i in range(1,50):
  for j in range(1,50):
    if 3**i + 5**j == n:
      count += 1
      a = i
      b = j
if count >= 1:
  print(a,b)
else:
  print(-1)

#B - Values

#Union Find
 
#xの根を求める
def find(x):
    if par[x] < 0:
        return x
    else:
        tank = []
        while par[x] >= 0:
            tank.append(x)
            x = par[x]
        for elt in tank:
            par[elt] = x
        return x
#xとyの属する集合の併合
def unite(x,y):
    x = find(x)
    y = find(y)
    
    if x == y:
        return False
    else:
        #sizeの大きいほうがx
        if par[x] > par[y]:
            x,y = y,x
        par[x] += par[y]
        par[y] = x
        return True
  
n,m = map(int,input().split())
a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))
 
par = [-1]*n
for i in range(m):
  c,d = map(int,input().split())
  unite(c-1,d-1)
 
tank = []
for i in range(n):
  tank.append(find(i))
max_num = max(tank)
a_part_list = [0 for i in range(max_num+1)]
b_part_list = [0 for i in range(max_num+1)]
for i in range(n):
  a_part_list[tank[i]] += a_list[i]
  b_part_list[tank[i]] += b_list[i]
 
if a_part_list == b_part_list:
  print('Yes')
else:
  print('No')

#C - Solutions

n,m = map(int, input().split())
if m < 0 or (n-m <= 1 and n >= 2):
  print(-1)
elif n == 1 and m == 0:
  print(1,2)
else:
  a = 2
  for i in range(m+1):
    print(a,a+1)
    a += 2
  print(1,a)
  a += 1
  x = n-m-2
  for i in range(x):
    print(a, a+x)
    a += 1