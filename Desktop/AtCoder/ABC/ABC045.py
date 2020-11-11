#ABC045(A〜D) A,B,C 完

#A - 台形

a = int(input())
b = int(input())
h = int(input())
print((a+b)*h//2)

#B - 3人でカードゲームイージー

x = input()
y = input()
z = input()
A_card = 0
B_card = 0
C_card = 0
turn = 'a'
while True:
  if turn == 'a':
    A_card += 1
    if A_card > len(x):
      print('A')
      exit()
    turn = x[A_card-1]
  elif turn == 'b':
    B_card += 1
    if B_card > len(y):
      print('B')
      exit()
    turn = y[B_card-1]
  else:
    C_card += 1
    if C_card > len(z):
      print('C')
      exit()
    turn = z[C_card-1]

#C - たくさんの数式

import itertools

s = input()
index = [i for i in range(1,len(s))]
ans = int(s)
for i in range(1,len(s)):
  for j in itertools.combinations(index,i):
    j = list(j)
    j.insert(0,0)
    j.append(len(s))
    for k in range(i+1):
      ans += int(s[j[k]:j[k+1]])
print(ans)