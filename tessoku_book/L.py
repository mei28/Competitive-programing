n, k = map(int, input().split())
A = list(map(int, input().split()))

ng = -1
ok = 10**8


def is_ok(m):
    cnt = 0
    for a in A:
        cnt += m // a
    if cnt >= k:
        return True
    else:
        return False


while ok - ng > 1:
    mid = (ok + ng) // 2

    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
