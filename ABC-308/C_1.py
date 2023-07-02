from functools import cmp_to_key


def cmp(a, b):
    x, y, i = a
    xx, yy, ii = b
    s = x * yy - y * xx
    return 1 if s > 0 else -1 if s < 0 else 0


n = int(input())
X = []
for i in range(n):
    a, b = map(int, input().split())
    X.append((-a, a + b, i + 1))

X.sort(key=cmp_to_key(cmp))
_, _, ans = zip(*X)
print(*ans)
