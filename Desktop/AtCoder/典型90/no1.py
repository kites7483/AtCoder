'''
point：答えで二分探索

left,right = (区間の最小)-1，(区間の最大)+1
while (right - left) > 1:
  mid = (left + right) // 2
  -----------------------
  各問題に合わせたコード
  -----------------------
  if 条件を満たす（満たさない）:
    left = mid
  else:
    right = mid
'''

#本題（Yokan Party）
#計算量（N*log(l)）

n,l = map(int,input().split())
k = int(input())
a_list = list(map(int,input().split()))

a_list.append(l)
for i in range(n):
  a_list[n-i] = a_list[n-i] - a_list[n-1-i]

left = -1
right = l+1
while (right - left) > 1:
  mid = (left + right) // 2
  length = 0
  count = 0
  for j in a_list:
    length += j
    if length >= mid:
      count += 1
      length = 0
  if count >= k+1:
    left = mid
  else:
    right = mid
print(left)