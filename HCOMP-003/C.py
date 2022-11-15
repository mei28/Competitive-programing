import math

a, b, x = map(int, input().split())

half = a * a * b / 2

if x < half:
    theta = math.atan(a * b * b / (2 * x))
else:
    theta = math.atan((2 * b - 2 * x / a**2) / a)

theta = theta / math.pi * 180
print(theta)
