#ABC065(A〜D) A,B,C 完

#A - Expired?

x,a,b = map(int, input().split())
if a >= b:
  print('delicious')
else:
  if b-a > x:
    print('dangerous')
  else:
    print('safe')

#B - Trained?

n = int(input())
line = [0]
for i in range(n):
  line.append(int(input()))
count = 1
light = 1
for i in range(10**5):
  if line[light] == 2:
    print(count)
    exit()
  light = line[light]
  count += 1
print(-1)

#C - Reconciled?

a,b = map(int, input().split())
mod = 10**9 + 7
if abs(b-a) > 1:
  print(0)
else:
  ans = 1
  for i in range(1,a+1):
    ans *= i
    ans %= mod
  for i in range(1,b+1):
    ans *= i
    ans %= mod
  if a != b:
    print(ans)
  else:
    print((2*ans)%mod)