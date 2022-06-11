from bisect import bisect_left, bisect_right

x, a, d, n = map(int, input().split())


def an(n):
    return a + d * (n - 1)


def check(mid):
    if (mid - a) // d == (mid - a) / d:
        return True
    else:
        return False


ok = 0
ng = d


while ok != ng:
    mid = (ok + ng) // 2
    print(mid)
    if d > 0:
        if check(mid):
            ok = mid
        else:
            ng = mid
    else:
        if not check(mid):
            ok = mid
        else:
            ng = mid


print(ok, ng)
