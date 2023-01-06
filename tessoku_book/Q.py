n = int(input())
A = [0] + list(map(int, input().split()))
B = [0, 0] + list(map(int, input().split()))

dp = [[0, ""] for _ in range(n + 5)]  # dp[i]: 部屋iに来るまでにかかる時間
# dp[i] = min(dp[i-1]+A_i,dp[i-2]+B_i,dp[i])


for i in range(1, n):
    if i == 1:
        dp[i][0] = dp[i - 1][0] + A[i]
        dp[i][1] = dp[i - 1][1] + "A"
    else:
        if dp[i - 1][0] + A[i] < dp[i - 2][0] + B[i]:
            dp[i][1] = dp[i - 1][1] + "A"
        else:
            dp[i][1] = dp[i - 2][1] + "B"
        dp[i][0] = min(dp[i - 1][0] + A[i], dp[i - 2][0] + B[i])

ans = [1]

for b in dp[n - 1][1]:
    if b == "B":
        ans.append(ans[-1] + 2)
    else:
        ans.append(ans[-1] + 1)

print(len(ans))
print(" ".join(ans))
