#ARC108(A〜F) 時間内：A 時間外：B 完

#A - Sum and Product

s,p = map(int,input().split())
x = s - ((s**2-4*p)**0.5)
y = s + ((s**2-4*p)**0.5)
if x != 0 and y != 0 and x % 2 == 0 and y % 2 == 0:
  print('Yes')
else:
  print('No')

#B - Abbreviate Fox

#方針：sの先頭から一文字ずつ取り出し，tの末尾に追加．tでfoxが揃ったら消去．
n = int(input())
s = input()
t = ''
for i in s:
  t = t + i
  if len(t) >= 3:
    if t[-3:] == 'fox':
      t = t[:-3]
print(len(t))