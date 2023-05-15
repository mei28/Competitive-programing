n = int(input())
A = list(map(int, input().split()))


def is_ok(m):
    tmp = [0 if a % m == 0 else 1 for a in A]
    print(m, tmp, sum(tmp))
    if sum(tmp) <= 1:
        return True
    return False


ok = 1
ng = 10**10

while ng - ok > 1:
    mid = (ok + ng) // 2

    if is_ok(mid):
        ok = mid
    else:
        ng = mid
print(ok)
