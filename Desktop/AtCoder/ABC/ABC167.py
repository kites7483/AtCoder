# A - Registration

a = input()
b = input()
if b[:-1] == a:
  print('Yes')
else:
  print('No')

# B - Easy Linear Programming

a,b,c,d = map(int, input().split())
if d < a:
  print(d)
elif d <= a + b:
  print(a)
else:
  print(a - (d - a - b))
