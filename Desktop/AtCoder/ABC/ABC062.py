#ABC062(A〜D) A,B 完

#A - Grouping

x,y = map(int,input().split())
line = [0,1,3,1,2,1,2,1,1,2,1,2,1]
if line[x] == line[y]:
  print('Yes')
else:
  print('No')

#B - Picture Frame

h,w = map(int, input().split())
print('#'*(w+2))
for i in range(h):
  print('#' + input() + '#')
print('#'*(w+2))
