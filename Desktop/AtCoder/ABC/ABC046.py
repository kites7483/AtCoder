#ABC046(A〜D) 全完

#A - AtCoDeerくんとペンキ

print(len(set(list(map(int, input().split())))))

#B - AtCoDeerくんとボール色塗り

n,k = map(int,input().split())
print(k*((k-1)**(n-1)))

#C - AtCoDeerくんと選挙速報

n = int(input())
count = 0
pre_t = 0
pre_a = 0
for i in range(n):
  t,a = map(int,input().split())
  x = t
  y = a
  if t+a < count:
    z = max(pre_t//t, pre_a//a)
    t *= z
    a *= z
  while True:
    if t+a >= count and t >= pre_t and a >= pre_a:
      count = t+a
      pre_t = t
      pre_a = a
      break
    else:
      t += x
      a += y
print(count)

#D - AtCoDeerくんと変なじゃんけん

from collections import Counter

s = Counter(input())
print((s['g'] - s['p']) // 2)