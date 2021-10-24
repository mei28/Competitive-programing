m = int(input())
G = [[0] * m for _ in range(m)]

for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1

    G[u][v] = 1
    G[v][u] = 1

P = map(int, input().split())
