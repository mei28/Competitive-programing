def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)


if __name__ == "__main__":
    dp = dict()
    n, d = map(int, input().split())
    dp = dict()
    for i in range(110):
        dp[i] = dp.setdefault(i, [0.0])

    dp[0][1] = 1
    for i in range(n):
        pass
    print()
