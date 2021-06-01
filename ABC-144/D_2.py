import math

PI = math.acos(-1.0)

a, b, x = map(int, input().split())
x /= a


def f(t):
    if math.tan(t) <= b / a:
        return a * b - a * (a * math.tan(t)) / 2
    else:
        return b * (b / math.tan(t)) / 2


ok = 0
ng = PI / 2

for i in range(180):
    theta = (ok + ng) / 2
    if f(theta) >= x:
        ok = theta
    else:
        ng = theta

print(ok * 180 / PI)
