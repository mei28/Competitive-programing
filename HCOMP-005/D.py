import math
from cmath import rect

n = int(input())
x0, y0 = map(int, input().split())
x2, y2 = map(int, input().split())

x, y = (x0 + x2) / 2, (y0 + y2) / 2

theta = 360 / n

a, b = x0 - x, y0 - y
res = (a + b * 1j) * rect(1, 2 * math.pi / n)

print(res.real + x, res.imag + y)
