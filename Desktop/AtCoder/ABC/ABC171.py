# A - alphabet

alpha = input()
if alpha.isupper():
  print('A')
else:
  print('a')

# B - Mix Juice

n,k = map(int, input().split())
line = list(map(int, input().split()))
line.sort()
sum = 0
for i in range(k):
  sum += line[i]
print(sum)

# C - One Quadrillion and One Dalmatians

n = int(input())
name = []
eng = 'abcdefghijklmnopqrstuvwxyz'
while n:
  name.append(eng[n % 26-1])
  if n % 26 == 0:
    n = n // 26 - 1
  else:
    n //= 26
print(''.join(reversed(name)))

# D - Replacing

n = int(input())
line_a = list(map(int,input().split()))
total = sum(line_a)
q = int(input())
numbers = [0 for i in range(10**5+1)]
for i in line_a:
  numbers[i] += 1

for i in range(q):
  b,c = map(int, input().split())
  d = c - b
  stock = numbers[b]
  numbers[c] += numbers[b]
  numbers[b] = 0
  total += stock*d
  print(total)