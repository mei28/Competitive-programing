import math

a, b, n = map(int, input().split())


def f(x):
    return math.floor(a * x / b) - a * math.floor(x / b)


l = 0
r = n + 1

while l + 10 ** (-3) < r:
    c1 = l + (r - l) / 3
    c2 = r - (r - l) / 3

    if f(c1) > f(c2):
        r = c2
    else:
        l = c1

ans = -(1 << 32)
for i in range(max(0, int(l) - 2), min(n, int(r) + 2) + 1):
    ans = max(ans, f(i))
print(ans)
