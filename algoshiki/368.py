n = int(input())


def calc(x):
    return x * (x * (x + 1) + 2) + 3


ok = 0
ng = 101

while (ng - ok) > 0.0001:
    mid = (ok + ng) / 2
    if calc(mid) <= n:
        ok = mid
    else:
        ng = mid
print(ok)
