# A - Multiplication 1

a,b = map(int, input().split())
print(a*b)

# B - Multiplication 2

n = int(input())
line = list(map(int, input().split()))
total = 1
if 0 in line:
  print(0)
else:
  for i in range(n):
    total *= line[i]
    if total > 10 ** 18:
      break;
  if total > 10 ** 18:
    print(-1)
  else:
    print(total)