h, w = map(int, input().split())
G = [["#"] * (w + 1) for _ in range(h + 1)]
dp = [[0] * (w + 1) for _ in range(h + 1)]

dp[1][1] = 1


for j in range(h):
    l = input()
    for i, r in enumerate(l):
        G[j + 1][i + 1] = r
for i in range(1, h + 1):
    for j in range(1, w + 1):
        if G[i][j] == "#":
            dp[i][j] = 0
            continue
        dp[i][j] = max(dp[i][j], dp[i - 1][j] + dp[i][j - 1])
print(dp[h][w])
