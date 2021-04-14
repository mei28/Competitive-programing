S = input()
MOD = 1000000007

# 状態DPを考える
# dp[pos][atcoderの何文字目までか]=通り

# dp[len(S)+100][len('atcoder')] = 0
dp = [[0 for _ in range(len("atcoder") + 10)] for _ in range(len(S) + 10)]

dp[0][0] = 1

for i in range(len(S)):
    for j in range(8):
        dp[i + 1][j] += dp[i][j]
        if S[i] == "a" and j == 0:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == "t" and j == 1:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == "c" and j == 2:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == "o" and j == 3:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == "d" and j == 4:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == "e" and j == 5:
            dp[i + 1][j + 1] += dp[i][j]
        if S[i] == "r" and j == 6:
            dp[i + 1][j + 1] += dp[i][j]

    for k in range(8):
        dp[i + 1][k] %= MOD

print(dp[len(S)][7])
