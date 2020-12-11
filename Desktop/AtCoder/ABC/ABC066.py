#ABC066(A〜D) A,B,C 完

#A - ringring

a,b,c = map(int,input().split())
print(min(a+b,b+c,c+a))

#B - ss

s = input()
x = len(s)
if x % 2 != 0:
  x -= 1
else:
  x -= 2
while True:
  if s[:x//2] == s[x//2:x]:
    print(x)
    exit()
  x -= 2

#C - pushpush

n = int(input())
line = list(map(int,input().split()))
A,B = [],[]
for i in range(n):
  if i % 2 == 0:
    A.append(line[i])
  else:
    B.append(line[i])
if n % 2 == 0:
  B.reverse()
  ans = [str(a) for a in B+A]
else:
  A.reverse()
  ans = [str(a) for a in A+B]
print(' '.join(ans))