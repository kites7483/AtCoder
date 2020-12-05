#ABC064(A〜D) 全完

#A - RGB Cards

a,b,c = map(int,input().split())
if (100*a + 10*b + c) % 4 == 0:
  print('YES')
else:
  print('NO')

#B - Traveling AtCoDeer Problem

n = int(input())
line = list(map(int,input().split()))
print(max(line) - min(line))

#C - Colorful Leaderboard

n = int(input())
line = list(map(int, input().split()))
colors = [0 for i in range(8)]
count = 0
for i in line:
  if i < 3200:
    colors[i//400] += 1
  else:
    count += 1
min_ans = 0
for i in colors:
  if i != 0:
    min_ans += 1
print(max(1,min_ans),min_ans + count)

#D - Insertion

n = int(input())
line = input()
stack = []
count = 0
for i in line:
  stack.append(i)
  if len(stack) >= 2:
    if stack[count-1] == '(' and stack[count] == ')':
      stack = stack[:count-1]
      count -= 2
  count += 1
x = 0
y = 0
for i in stack:
  if i == '(':
    x += 1
  else:
    y += 1
print('(' * y + line + ')' * x)