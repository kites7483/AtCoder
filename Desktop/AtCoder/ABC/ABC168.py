# A - ∴ (Therefore)

a = input()
if a[-1] == "3":
  print("bon")
elif a[-1] == "0" or a[-1] == "1" or a[-1] == "6" or a[-1] == "8":
  print("pon")
else:
  print("hon")

# B - ... (Triple Dots)

k = int(input())
s = input()
if len(s) <= k:
  print(s)
else:
  print(s[:k] + "...")

# C - : (Colon)

import math

a,b,h,m = map(float, input().split())
theta1 = (h*60 + m)/2
theta2 = m*6
theta = theta1 - theta2
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))
print(c)