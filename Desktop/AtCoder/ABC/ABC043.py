#ABC043(A〜D) 全完

#A - キャンディーとN人の子供イージー

n = int(input())
print(n*(n+1) // 2)

#B - バイナリハックイージー

s = input()
ans = []
for i in s:
  if i == '0' or i == '1':
    ans.append(i)
  else:
    if ans != []:
      ans.pop()
print(''.join(ans))

#C - いっしょ

n = int(input())
line = list(map(int, input().split()))
ans = 10**10
for i in range(-100,101):
  count = 0
  for j in line:
    count += (i-j)**2
  if count < ans:
    ans = count
print(ans)

#D - アンバランス

s = input()

for i in range(len(s)-1):
  if s[i] == s[i+1]:
    print(i+1,i+2)
    exit()
    
for i in range(len(s)-2):
  if s[i] == s[i+2]:
    print(i+1,i+3)
    exit()
    
print(-1,-1)