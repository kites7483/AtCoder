#A - 和風いろはちゃんイージー

line = list(map(int, input().split()))
if line == [5,7,5] or line == [7,5,5] or line == [5,5,7]:
  print('YES')
else:
  print('NO')

#B - 文字列大好きいろはちゃんイージー

n,l = map(int,input().split())
word_list = []
for i in range(n):
  word_list.append(input())
word_list.sort()
print(''.join(word_list))

#C - こだわり者いろはちゃん

from collections import Counter

n,k = map(int,input().split())
line = ''.join(list(map(str, input().split())))
while True:
  if Counter(str(n)) - Counter(line) == Counter(str(n)):
    print(n)
    exit()
  n += 1

#D - いろはちゃんとマス目

def comb(n,r,mod):
  if (r < 0 or r > n):
    return 0
  r = min(r,n-r)
  return g1[n] * g2[r] * g2[n-r] % mod

mod = 10**9+7 #出力の制限
N = 2*10**5 #nの最大値
g1 = [1,1] #元テーブル
g2 = [1,1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range(2,N+1):
  g1.append(( g1[-1] * i ) % mod) #(インデックス番号)!のmod
  inverse.append(( -inverse[mod % i] * (mod//i) ) % mod)
  g2.append((g2[-1] * inverse[-1]) % mod)

h,w,a,b = map(int,input().split())
ans = 0
for i in range(h-a):
  ans += comb(b-1+i,i,mod) * comb(h-i-1+w-b-1,w-b-1,mod)
  ans %= 10**9+7
print(ans)