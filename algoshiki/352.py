n, a, b = map(int, input().split())
X = list(map(int, input().split()))

# dp[i][j]: 最初のi舞だけ使ってその総和がaで割った時にj余るかどうか

dp = [[False] * a for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(a):
        if not dp[i][j]:
            continue

        dp[i + 1][j] = True
        dp[i + 1][(j + X[i]) % a] = True

if dp[n][b]:
    print("Yes")
else:
    print("No")
