n = int(input())
x, y = map(int, input().split())

A, B = [], []
AB = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    AB.append([a, b])

# dp[i][x][y] : i種類までにx,y になるときに少なくとも何個で行けるか

INF = 1 << 60
dp = [[[INF] * (302) for _ in range(302)] for _ in range(302)]
dp[0][0][0] = 0

for i in range(n):
    a, b = A[i], B[i]
    for j in range(x + 1):
        for k in range(y + 1):
            jj = min(j + a, x)
            kk = min(k + b, y)

            dp[i + 1][j][k] = min(dp[i + 1][j][k], dp[i][j][k])

            dp[i + 1][jj][kk] = min(dp[i + 1][jj][kk], dp[i][j][k] + 1)


if dp[n][x][y] < INF:
    print(dp[n][x][y])
else:
    print(-1)
