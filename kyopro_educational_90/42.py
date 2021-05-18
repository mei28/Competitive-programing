K = int(input())
MOD = 1000000007

if K % 9 != 0:
    print(0)
    exit()

# dp[i: 核桁の数字の和]=通り数
dp = [0] * (K + 10)
dp[0] = 1

for i in range(K + 1):
    b = min(i, 9)
    for j in range(1, b + 1):
        dp[i] += dp[i - j]
        dp[i] %= MOD

print(dp[K])
