N, P = map(int, input().split())

dp = [[0 for _ in range(P + 10)] for _ in range(N + 10)]
MOD = 1000000007


def show(dp):
    print("-" * 20)
    for i in dp:
        print(i)


dp[0][0] = 1
for k in range(1, P):
    for i in range(N + 1):
        for j in range(P):
            tmp = (j + k) % MOD
            dp[i + 1][tmp] += dp[i][j]
        for j in range(P):
            dp[i][j] %= MOD

    show(dp)

ans = 0

for i in range(P + 1):
    ans += dp[N - 1][i]

print(ans)
