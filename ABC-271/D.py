n, s = map(int, input().split())
A = []
for _ in range(n):
    a, b = map(int, input().split())
    A.append((a, b))

# dp[i][j]: i番までつかってjになるかどうか

dp = [[False for _ in range(s + 10)] for _ in range(n + 1)]
dp[0][0] = True
pp = [["" for _ in range(s + 10)] for _ in range(n + 1)]
for i in range(n + 1):
    dp[i][0] = True

for i in range(n):
    for j in range(s + 2):
        if j - A[i][0] >= 0:
            if dp[i - 1][j - A[i][0]] and len(pp[i - 1][j - A[i][0]]) == i:
                pp[i][j] = pp[i - 1][j - A[i][0]] + "H"
                dp[i][j] = True
        if j - A[i][1] >= 0:
            if dp[i - 1][j - A[i][1]] and len(pp[i - 1][j - A[i][1]]) == i:
                pp[i][j] = pp[i - 1][j - A[i][1]] + "T"
                dp[i][j] = True
if dp[n - 1][s] and len(pp[n - 1][s]) == n:
    print("Yes")
    print(pp[n - 1][s])
else:
    print("No")
