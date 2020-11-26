#ABC057(A〜D) A,B,C 完

#A - Remaining Time

a,b = map(int,input().split())
print((a+b)%24)

#B - Checkpoints

n,m = map(int,input().split())
n_list = [list(map(int,input().split())) for i in range(n)]
m_list = [list(map(int,input().split())) for i in range(m)]
for student in n_list:
  min_dis = 10**10
  for j in range(m):
    dis = abs(student[0]-m_list[j][0]) + abs(student[1]-m_list[j][1])
    if min_dis > dis:
      min_dis = dis
      index = j+1
  print(index)

#C - Digits in Multiplication

n = int(input())
ans = 15
for a in range(1,int(n**(1/2))+1):
  if n % a == 0:
    b = n // a
    f = max(len(str(a)),len(str(b)))
    if ans > f:
      ans = f
print(ans)