n = int(input())
A = list(map(int, input().split()))
A.sort()

MOD = 998244353
ans = 0

# dp[i][j][k]: iまでみてjこえらんだとき
def solve(M):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[0][0] = 1
    for a in A:
        for j in range(n, 0, -1):
            for k in range(M):
                dp[j][k] += dp[j - 1][(k - a) % M]
                dp[j][k] %= MOD
    return dp[M][0]


for cnt in range(1, n + 1):
    ans += solve(cnt)

print(ans)    
