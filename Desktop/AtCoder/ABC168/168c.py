import math

a,b,h,m = map(float, input().split())
theta1 = (h*60 + m)/2
theta2 = m*6
theta = theta1 - theta2
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(math.radians(theta)))
print(c)
