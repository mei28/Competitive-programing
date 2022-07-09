import math
a, b, d = map(int, input().split())

rad = math.radians(d)
rx = a*math.cos(rad) - b * math.sin(rad)
ry = a*math.sin(rad) + b * math.cos(rad)
print(rx,ry)
