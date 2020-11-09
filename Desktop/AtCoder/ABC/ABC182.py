#A - twiblr

a,b = map(int,input().split())
print(2*a+100-b)

#B - Almost GCD

n = int(input())
line = list(map(int, input().split()))
ans = 0
max_count = 0
for i in range(2,1001):
  count = 0
  for j in line:
    if j % i == 0:
      count += 1
  if count > max_count:
    max_count = count
    ans = i
print(ans)

#C - To 3

s = input()
if int(s) % 3 == 0:
  print(0)

else:
  count = 0
  line = [0 for i in range(3)]
  for i in s:
    count += int(i)
    line[int(i)%3] += 1

  if count < 3:
    print(-1)
    exit()

  if count % 3 == 1:
    if line[1] >= 1 and len(s) >= 2:
      print(1)
    elif line[2] >= 2 and len(s) >= 3:
      print(2)
    else:
      print(-1)
    exit()

  if count % 3 == 2:
    if line[2] >= 1 and len(s) >= 2:
      print(1)
    elif line[1] >= 2 and len(s) >= 3:
      print(2)
    else:
      print(-1)
    exit()

#D - Wandering

n = int(input())
line = list(map(int, input().split()))
ans = 0
for i in range(n-1):
  line[i+1] += line[i]
point = 0
positive_max = 0
point_list = [0]
for i in range(n):
  if line[i] > positive_max:
    positive_max = line[i]
  point_list.append(point + positive_max)
  point += line[i]
print(max(point_list))