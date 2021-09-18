n = int(input())
x, y = map(int, input().split())

A, B = [], []
AB = []
for i in range(n):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    AB.append([a, b])

# dp[i][x][y] : x,y になるときに少なくとも何個で行けるか

INF = 1 << 60
dp = [[[INF] * (302) for _ in range(302)] for _ in range(302)]
dp[0][0][0] = 0

for i in range(n):
    for _x in range(x + 1):
        for _y in range(y + 1):
            dp[i + 1][_x][_y] = min(dp[i + 1][_x][_y], dp[i][_x][_y])
            if _x >= AB[i][0] and _y >= AB[i][1]:
                dp[i + 1][_x][_y] = min(
                    dp[i + 1][_x][_y], dp[i][_x - AB[i][0]][_y - AB[i][1]] + 1
                )

if dp[n][x][y] < INF:
    print(dp[n][x][y])
else:
    print(-1)
