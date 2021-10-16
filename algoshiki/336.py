n, m = map(int, input().split())
A = list(map(int, input().split()))

dp = [[False] * m for _ in range(n)]
# dp[i][j]: (i,j)に駒が存在することがあるか
# (i,j)にいる時, (i+1,j)もしくは(i+1,j+A[i])にいる可能性がある

dp[0][0] = True

for i in range(n - 1):
    for j in range(m):
        if not dp[i][j]:
            continue

        dp[i + 1][j] = True
        if j + A[i] < m:
            dp[i + 1][j + A[i]] = True

print(sum(dp[-1]))
