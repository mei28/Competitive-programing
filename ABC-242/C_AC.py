n:int = int(input())
MOD = 998244353

dp = [[0]*9 for _ in range(n+10)]

dp[0] = [1]*9


for i in range(1,n):
    for d in range(9):
        if d-1>=0:
            dp[i][d] += dp[i-1][d-1]

        dp[i][d] += dp[i-1][d]
        
        if d+1<9:
            dp[i][d] += dp[i-1][d+1]

        dp[i][d]%=MOD

print(sum(dp[n-1]) %MOD)
