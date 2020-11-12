#ABC047(A〜D) 全完

#A - キャンディーと2人の子供

a,b,c = map(int,input().split())
if a+b == c or b+c == a or c+a == b:
  print('Yes')
else:
  print('No')

#B - すぬけ君の塗り絵 2 イージー

w,h,n = map(int, input().split())
a_1,a_2,a_3,a_4 = [0],[w],[0],[h]
for i in range(n):
  x,y,a = map(int, input().split())
  if a == 1:
    a_1.append(x)
  elif a == 2:
    a_2.append(x)
  elif a == 3:
    a_3.append(y)
  else:
    a_4.append(y)
    
if (min(a_2) - max(a_1)) <= 0 or (min(a_4) - max(a_3)) <= 0:
  print(0)
else:
  print((min(a_2) - max(a_1)) * (min(a_4) - max(a_3)))

#C - 一次元リバーシ

s = input()
count = 0
x = s[0]
for i in s[1:]:
  if i != x:
    count += 1
    x = i
print(count)

#D - 高橋君と見えざる手

n,t = map(int,input().split())
line = list(map(int,input().split()))
price_min = line[0]
profit_max = 0
ans = 0
for i in range(1,n):
  if line[i] - price_min == profit_max:
    ans += 1
  elif line[i] - price_min > profit_max:
    profit_max = line[i] - price_min
    ans = 1
  if line[i] < price_min:
    price_min = line[i]
print(ans)