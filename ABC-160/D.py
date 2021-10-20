from collections import deque

n, x, y = map(int, input().split())
G = [[] for _ in range(n)]

for i in range(n - 1):
    G[i].append(i + 1)
    G[i + 1].append(i)

G[x - 1].append(y - 1)
G[y - 1].append(x - 1)

dist = [[1e20] * n for _ in range(n)]


def getdist(start: int) -> None:
    for i in range(n):
        dist[start][i] = 1e20

    que = deque()
    que.append(start)
    dist[start][start] = 0

    while len(que) > 0:
        pos = que.popleft()
        for to in G[pos]:
            if dist[start][to] >= 1e18:
                dist[start][to] = dist[start][pos] + 1

                que.append(to)


for i in range(n):
    getdist(i)


for i in range(1, n):
    cnt = 0
    for d in dist:
        cnt += sum(map(lambda x: x == i, d))

    print(cnt // 2)
