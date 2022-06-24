n, m = map(int, input().split())
INF = 1 << 30
G = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(n + 1):
    G[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    G[a][b] = c


ans = 0
for k in range(1, n + 1):
    D = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            D[i][j] = min(G[i][j], G[i][k] + G[k][j])

            if D[i][j] != 1 << 30:
                ans += D[i][j]
    G = D

print(ans)
