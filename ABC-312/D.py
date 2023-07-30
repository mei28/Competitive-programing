def solve(S):
    mod = 998244353
    n = len(S)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for i in range(n):
        for j in range(i + 1):
            if S[i] in ["(", "?"]:
                dp[i + 1][j + 1] += dp[i][j]
                dp[i + 1][j + 1] %= mod
            if S[i] in [")", "?"]:
                if j > 0:
                    dp[i + 1][j - 1] += dp[i][j]
                    dp[i + 1][j - 1] %= mod
    return dp[n][0]


S = input().strip()
print(solve(S))
