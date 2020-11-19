#ABC053(A〜D) 全完

#A - ABC/ARC

n = int(input())
if n < 1200:
  print('ABC')
else:
  print('ARC')

#B - A to Z String

s = input()
x = len(s)
for i in range(x):
  if s[i] == 'A':
    break
for j in range(-1,(-1)*x,-1):
  if s[j] == 'Z':
    break
print(x+j-i+1)

#C - X: Yet Another Die Game

x = int(input())
a = x//11
if x % 11 == 0:
  print(2*a)
elif x-11*a > 6:
  print(2*a+2)
else:
  print(2*a+1)

#D - Card Eater

from collections import Counter

n = int(input())
card_list = list(map(int,input().split()))
cards = dict(Counter(card_list))
count = 0
for i in cards.values():
  if i % 2 == 0:
    count += 1
if count % 2 == 0:
  print(len(cards))
else:
  print(len(cards)-1)