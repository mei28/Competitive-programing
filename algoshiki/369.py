n, k = map(int, input().split())
L = list(map(int, input().split()))
L.sort()

ok = 0
ng = max(L) + 1


def is_ok(x):
    cnt = 0
    for l in L:
        cnt += l // x
    return cnt >= k


while ng - ok > 0.0000001:
    mid = (ok + ng) / 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(ok)
