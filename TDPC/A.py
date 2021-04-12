N = int(input())
P = list(map(int, input().split()))

# dp[i][j]: i問目よりも前にj点取れるかどうか

dp = [[False for _ in range(11000)] for _ in range(110)]

dp[0][0] = True

for i in range(1, N + 1):
    for j in range(11000):
        dp[i][j] = dp[i - 1][j]
        if j - P[i - 1] >= 0:
            dp[i][j] |= dp[i - 1][j - P[i - 1]]

ans = 0

for j in range(11000):
    if dp[N][j]:
        ans += 1

print(ans)
