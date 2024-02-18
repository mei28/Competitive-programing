n = int(input())

dp = [-1] * (n + 10)

dp[0] = 0


def get_canditate(_n: int):
    ret = set()
    ret.add(1)

    tmp = 6
    while tmp <= _n:
        ret.add(tmp)
        tmp *= 6

    tmp = 9
    while tmp <= _n:
        ret.add(tmp)
        tmp *= 9

    ret = list(ret)
    ret.sort()
    return ret


for i in range(n + 2):
    candidates = get_canditate(n)

    for c in candidates:
        if dp[i - c] < 0:
            continue
        if dp[i] < 0:
            dp[i] = dp[i - c] + 1
            continue
        dp[i] = min(dp[i - c] + 1, dp[i])

print(dp[n])
