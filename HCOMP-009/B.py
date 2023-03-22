n = int(input())
ok = 0
ng = n + 1


def is_ok(mid):
    return (mid + 1) * mid // 2 <= n + 1


while ng - ok > 1:
    mid = (ok + ng) // 2

    if is_ok(mid):
        ok = mid
    else:
        ng = mid

print(n - ok + 1)
