from bisect import bisect_left

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

AB = [[a, b] for a, b in zip(A, B)]
AB = list(sorted(AB, key=lambda x: x[0]))


def lower_bound(x, C):
    ok = 0
    ng = n
    while ng - ok > 1:
        mid = (ng + ok) // 2
        if C[mid] < x:
            ok = mid
        else:
            ng = mid
    return ok


def LIS(C):
    # dp[i]:= 長さi+1の部分ボジ列の末尾としてありえる最小値
    dp = []
    for x in C:
        i = bisect_left(C, x)
        if i >= len(dp):
            dp.append(x)
        else:
            dp[i] = x
    return len(dp)


C = [x[1] for x in AB]

print(n + LIS(C))
