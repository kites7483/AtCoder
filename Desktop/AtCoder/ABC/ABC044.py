#ABC044(A〜D) A,B,C 完

#A - 高橋君とホテルイージー

n = int(input())
k = int(input())
x = int(input())
y = int(input())
if n <= k:
  print(n*x)
else:
  print(k*x + (n-k)*y)

#B - 美しい文字列

from collections import Counter

words = Counter(input())
for v in words.values():
  if v % 2 != 0:
    print('No')
    exit()
print('Yes')

#C - 高橋君とカード (DP)

n,a = map(int,input().split())
line1 = list(map(int, input().split()))
line2 = [0 for i in range(n+1)]
for i in range(n):
  line2[i+1] = line1[i] - a #データを一律でずらす
x = max(max(line1),a)
dp = [[0 for i in range(2*n*x+1)] for i in range(n+1)] #配列用意

#dp[i][j] : line2[0]〜line2[i]から0枚以上選んだときの合計がj-nxになる組み合わせの数

for i in range(n+1):
  for j in range(2*n*x+1):
    if i == 0 and j == n*x:
      dp[i][j] = 1 #0枚選べば総和も0
    elif i >= 1 and (j-line2[i] < 0 or j-line2[i] > 2*n*x):
      dp[i][j] = dp[i-1][j] #line2[i]を選んだら条件を満たせなくなる
    elif i >= 1 and j-line2[i] >= 0 and j-line2[i] <= 2*n*x:
      dp[i][j] = dp[i-1][j] + dp[i-1][j-line2[i]] #line2[i]を選ばない時 + line2[i]を選ぶ時
    else:
      dp[i][j] = 0
print(dp[n][n*x] - 1) #条件を満たす数