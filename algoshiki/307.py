n, m = map(int, input().split())
Ds = list(map(int, input().split()))

dp = [0] * (n + 1)
# dp[i]: iまでに到達できるか?
# dp[i] = dp[i-d] + 1

dp[0] = 1
for i in range(n + 1):
    for d in Ds:
        if i - d >= 0 and dp[i - d] != 0:
            dp[i] = dp[i - d]

print("Yes" if dp[n] != 0 else "No")
