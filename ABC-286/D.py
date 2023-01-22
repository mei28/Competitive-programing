n, x = map(int, input().split())
A = [0]
B = [0]
m = max(B) + 1
for _ in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

# dp[n][k]: n種類でkになるか?
dp = [[False] * (x + 1) for _ in range(n + 1)]

dp[0][0] = True

# dp[i][k] |= dp[i-1][k]
# dp[i][k] |= dp[i-1][k-a]
for i in range(1, n + 1):
    a, b = A[i], B[i]
    for k in range(x + 1):
        for j in range(b + 1):
            dp[i][k] |= dp[i - 1][k]
            if k - j * a >= 0:
                dp[i][k] |= dp[i - 1][k - j * a]
print("Yes" if dp[n][x] else "No")
