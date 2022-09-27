n, k = map(int, input().split())
A = list(map(int, input().split()))

ok = 0
ng = 10**13


def is_ok(mid):
    s = 0
    for i in range(n):
        s += min(mid, A[i])
    if s <= k:
        return True
    else:
        return False


while ng - ok > 1:
    mid = (ok + ng) // 2
    if is_ok(mid):
        ok = mid
    else:
        ng = mid

for i in range(n):
    d = min(ok, A[i])
    A[i] -= d
    k -= d

for i in range(n):
    if k == 0:
        break
    if A[i] > 0:
        A[i] -= 1
        k -= 1

print(*A)
