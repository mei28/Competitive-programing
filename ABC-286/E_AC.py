n = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(n)]

INF = 1 << 30
dist = [[(INF, INF) * n for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if S[i][j] == "Y":
            dist[i][j] = (1, -A[i])


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], add(dist[i][k], dist[k][j]))

q = int(input())
for _ in range(q):
    u, v = map(lambda x: int(x) - 1, input().split())
    cost = dist[u][v][0]
    val = -dist[u][v][1]
    if val == -INF:
        print("Impossible")
    else:
        print(cost, val + A[v])
