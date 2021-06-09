N, M = map(int, input().split())
A = []
is_safe = [True] * (N + 10)
MOD = 1000000007
for _ in range(M):
    is_safe[int(input())] = False

dp = [0] * (N + 100)

dp[0] = 1
for i in range(1, N + 10):

    if not is_safe[i]:
        dp[i] == 0
        continue
    if i == 1:
        dp[i] += dp[i - 1]
    else:
        dp[i] += dp[i - 1] + dp[i - 2]

    dp[i] %= MOD
print(dp[N])
