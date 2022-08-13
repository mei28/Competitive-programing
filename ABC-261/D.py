from collections import defaultdict

n, m = map(int, input().split())
X = list(map(int, input().split()))
CY = [list(map(int, input().split())) for _ in range(m)]
INF = 1 << 30
dct = defaultdict(int)
for c, y in CY:
    dct[c] += y

# dp[i][j] = i日目にカウンタがjの時の最大のお金
# 表の時
# dp[i][j] = dp[i-1][j-1] + X[i] + dct[i]
# 裏の時
# dp[i][0] = max(dp[i][j])

ma = [-1] * (5010)

dp = [[-INF] * (5010) for _ in range(5010)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(1, i + 1):
        # 表の時
        dp[i][j] = dp[i - 1][j - 1] + X[i - 1] + dct[j]

    dp[i][0] = 0
    for j in range(0, i + 1):
        dp[i][0] = max(dp[i][0], dp[i - 1][j])

ans = 0
for i in range(0, n + 1):
    ans = max(ans, dp[n][i])

print(ans)
