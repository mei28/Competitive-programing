n = int(input())
A = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] = i日目に仕事jを選んだ時の報酬

dp = [[0] * 3 for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(3):
        a = (j + 1) % 3
        b = (j + 2) % 3
        dp[i][j] = A[i - 1][j] + max(dp[i - 1][a], dp[i - 1][b])

print(max(dp[-1]))
