#ABC056(A〜D) A,B,C 完

#A - HonestOrDishonest

a,b = map(str,input().split())
if a == 'H':
  print(b)
else:
  if b == 'H':
    print('D')
  else:
    print('H')

#B - NarrowRectanglesEasy

w,a,b = map(int,input().split())
if a <= b:
  if a+w >= b:
    print(0)
  else:
    print(b-(a+w))
else:
  if b+w >= a:
    print(0)
  else:
    print(a-(b+w))

#C - Go Home

x = int(input())
for i in range(100000):
  if i*(i+1)/2 < x and x <= (i+1)*(i+2)/2:
    print(i+1)
    exit()