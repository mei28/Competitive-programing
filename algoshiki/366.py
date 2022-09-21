n = int(input())
X = list(map(int, input().split()))


def calc(x):
    return (1 + x) * x // 2


for x in X:
    ok = 10**15
    ng = -1

    while ok - ng > 1:
        mid = (ok + ng) // 2
        if x <= calc(mid):
            ok = mid
        else:
            ng = mid
    print(ok)
