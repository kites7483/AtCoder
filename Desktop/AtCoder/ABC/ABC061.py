#ABC061(A〜D) A,B,C 完

#A - Between Two Integers

a,b,c = map(int,input().split())
if a <= c and b >= c:
  print('Yes')
else:
  print('No')

#B - Counting Roads

n,m = map(int, input().split())
ans = [0 for i in range(n)]
for j in range(m):
  a,b = map(int, input().split())
  ans[a-1] += 1
  ans[b-1] += 1
for i in range(n):
  print(ans[i])

#C - Big Array

n,k = map(int,input().split())
number_list = [0 for i in range(10**5+1)]
for i in range(n):
  a,b = map(int,input().split())
  number_list[a] += b
  
for i in range(10**5):
  number_list[i+1] += number_list[i]

for i in range(10**5):
  if number_list[i] < k and k <= number_list[i+1]:
    print(i+1)
    exit()