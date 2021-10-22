a, b, c = map(int, input().split())
_max = a + b + c

A = [a, b, c]
A.sort()
a, b, c = A
_min = 0 if a + b > c else c - a - b


import math

PI = math.pi

ans = (_max ** 2 - _min ** 2) * PI
print(ans)
