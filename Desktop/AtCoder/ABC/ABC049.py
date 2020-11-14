#ABC049(A〜D) A,B,C 完

#A - 居合を終え、青い絵を覆う

s = input()
vowels = ['a','i','u','e','o']
if s in vowels:
  print('vowel')
else:
  print('consonant')

#B - たてなが

h,w = map(int,input().split())
for i in range(h):
  s = input()
  print(s)
  print(s)

#C - 白昼夢

s = input()
s_reverse = s[::-1]
while s_reverse != '':
  if s_reverse[:5] == 'esare' or s_reverse[:5] == 'maerd':
    s_reverse = s_reverse[5:]
  elif s_reverse[:6] == 'resare':
    s_reverse = s_reverse[6:]
  elif s_reverse[:7] == 'remaerd':
    s_reverse = s_reverse[7:]
  else:
    print('NO')
    exit()
print('YES')