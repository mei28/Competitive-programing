n = 1 << 20

p = [-1] * (n + 1)
A = [-1] * (n)


def root(x: int) -> int:
    if p[x] < 0:
        return x
    p[x] = root(p[x])
    return p[x]


def merge(x: int, y: int):
    x = root(x)
    y = root(y)
    if x == y:
        return
    if x < y:
        x, y = y, x
    p[x] += p[y]
    p[y] = x


q = int(input())

for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        h = x % n
        target = root(h)
        if target == n:
            target = root(0)
        A[target] = x
        merge(target, target + 1)

    if t == 2:
        print(A[x % n])
