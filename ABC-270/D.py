n, k = map(int, input().split())
A = list(map(int, input().split()))

dp = [0] * 10010
for i in range(n + 1):
    for j in range(k):
        if A[j] > i:
            break
        dp[i] = max(dp[i], i - dp[i - A[j]])
print(dp[n])
