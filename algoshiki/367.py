n, m = map(int, input().split())

ok = 1
ng = 100000000000000


def calc(i, a, x):
    a = a * x + 1
    if i >= 5:
        return a
    else:
        return calc(i + 1, a, x)


while (ng - ok) > 0.00001:
    mid = (ok + ng) / 2
    if calc(1, n + 1, mid) <= m:
        ok = mid
    else:
        ng = mid
print(ok)
