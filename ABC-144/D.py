import math

a, b, x = map(int, input().split())
PI = math.acos(-1.0)
x /= a

if x > a * b / 2:
    print(math.atan2((a * b - x) * 2, a * a) * 180 / PI)
else:
    print(math.atan2(b * b, x * 2) * 180 / PI)
