#ABC063(A〜D) A,B,C 完

#A - Restricted

a,b = map(int,input().split())
if a + b >= 10:
  print('error')
else:
  print(a+b)

#B - Varied

s = input()
letters = []
for i in s:
  if i in letters:
    print('no')
    exit()
  else:
    letters.append(i)
print('yes')

#C - Bugged

n = int(input())
count = 0
line = []
for i in range(n):
  a = int(input())
  line.append(a)
line.sort()

for i in range(n):
  if line[i] % 10 != 0:
    count += 1
    break
    
total = sum(line)
if total % 10 != 0:
  print(total)
else:
  if count == 0:
    print(0)
  else:
    print(total-line[i])