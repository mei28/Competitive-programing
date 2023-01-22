N = int(input())
A = list(map(int, input().split()))
S = [input() for _ in range(N)]
INF = 10**18
dist = [[(INF, INF)] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if S[i][j] == "Y":
            dist[i][j] = (1, -A[i])


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


for k in range(N):
    for i in range(N):
        for j in range(N):
            dist[i][j] = min(dist[i][j], add(dist[i][k], dist[k][j]))


Q = int(input())
for _ in range(Q):
    U, V = map(int, input().split())
    U -= 1
    V -= 1
    d = dist[U][V][0]
    cost = dist[U][V][1]
    if cost == INF:
        print("Impossible")
    else:
        print(d, -cost + A[V])
