MOD = 998244353
n,m,k=map(int,input().split())

dp = [[0]*(k+1) for _ in range(n+1)]
# dp[i][j]：先頭iこうまでで合計がjになるやつの合計数

dp[0][0] = 1

for i in range(n):
    for j in range(k+1):
        for o in range(1,m+1):
            if j+o <=k:
                dp[i+1][j+o] += dp[i][j]
                dp[i+1][j+o] %= MOD

ans = 0

for i in range(k+1):
    ans += dp[n][i]
    ans %= MOD

print(ans)
