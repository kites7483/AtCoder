#ABC050(A〜D) A,B,C 完

#A - Addition and Subtraction Easy

a,b,c = map(str, input().split())
if b == '+':
  print(int(a) + int(c))
else:
  print(int(a) - int(c))

#B - Contest with Drinks Easy

n = int(input())
T_list = list(map(int,input().split()))
ans = sum(T_list)
m = int(input())
for i in range(m):
  p,x = map(int,input().split())
  print(ans - (T_list[p-1] - x))

#C - Lining Up

n = int(input())
A_list = list(map(int,input().split()))
A_list.sort()
mod = 10**9 + 7
if n % 2 == 0:
  correct_list = []
  for i in range(n//2):
    correct_list.append(2*i+1)
    correct_list.append(2*i+1)
  if correct_list != A_list:
    print(0)
  else:
    print(2**(n//2) % mod)
else:
  correct_list = [0]
  for i in range(n//2):
    correct_list.append(2*i+2)
    correct_list.append(2*i+2)
  if correct_list != A_list:
    print(0)
  else:
    print(2**(n//2) % mod)