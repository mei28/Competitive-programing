S = input()
T = input()

dp = [[0] * (len(T) + 1) for _ in range(len(S) + 1)]

for i in range(1, len(S) + 1):
    s = S[i - 1]
    for j in range(1, len(T) + 1):
        t = T[j - 1]

        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        if s == t:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
print(dp[-1][-1])
