MOD = 1000000007

s = int(input())
dp = [0] * (s + 1)

# dp[i]: iになる時のパターンの数
# dp[i] = dp[0]+...dp[i-3]

dp[0] = 1

if s <= 2:
    print(dp[s])
    exit()

for i in range(s + 1):
    for j in range(i - 2):
        dp[i] = dp[i] + dp[j]
        dp[i] %= MOD

print(dp[s])
