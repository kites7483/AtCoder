#ABC058(A〜D) A,B,C 完

#A - ι⊥l

a,b,c = map(int,input().split())
if b-a == c-b:
  print('YES')
else:
  print('NO')

#B - ∵∴∵

o = input()
e = input()
if len(o)-len(e) == 0:
  for i in range(len(o)):
    print(o[i],end="")
    print(e[i],end="")
else:
  for i in range(len(e)):
    print(o[i],end="")
    print(e[i],end="")
  print(o[i+1],end="")
print()

#C - 怪文書

import numpy as np

n = int(input())
matrix = []
for i in range(n):
  s = input()
  line = [0 for i in range(26)]
  for j in s:
    line[ord(j)-97] += 1
  matrix.append(line)
matrix = np.array(matrix)
min_list = np.min(matrix, axis=0)
for i in range(26):
  print(chr(i+97) * min_list[i], end="")
print()