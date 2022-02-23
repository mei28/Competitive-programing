n, x = map(int, input().split())

dp = [[False] * 10010 for _ in range(110)]

dp[0][0] = True

AB = [list(map(int, input().split())) for _ in range(n)]


for i in range(n):
    a, b = AB[i]
    for j in range(x + 10):
        if dp[i][j] == True:
            if j + a <= x:
                dp[i + 1][j + a] = True
            if j + b <= x:
                dp[i + 1][j + b] = True

print("Yes" if dp[n][x] else "No")
