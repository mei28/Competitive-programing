from collections import deque

n, q = map(int, input().split())
G = [[] for _ in range(n + 1)]
E = []

for i in range(n - 1):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

dist = [1e20] * (n + 1)


def getdist(start: int):
    for i in range(0, n + 1):
        dist[i] = 1e20

    q = deque()
    q.append(start)
    dist[start] = 0

    while len(q) > 0:
        pos = q.popleft()
        for to in G[pos]:
            if dist[to] >= 1e19:
                dist[to] = dist[pos] + 1
                q.append(to)
    return dist


dist_all = [[] for _ in range(n + 1)]

for i in range(1, n + 1):
    d = getdist(i)
    dist_all[i] = d


for i in range(q):
    c, d = map(int, input().split())

    diff = dist_all[c][d]

    if diff % 2 != 0:
        print("Road")
    else:
        print("Twon")
