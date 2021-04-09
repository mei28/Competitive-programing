from collections import deque

N = int(input())
A, B = [], []
G = [[] for _ in range(N)]
dist = [1e20] * N


def getdist(start: int):
    # BFSによって最短距離を求める
    for i in range(N):
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


for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    A.append(a)
    B.append(b)
    G[a].append(b)
    G[b].append(a)

getdist(0)
maxn1 = -1
maxid1 = -1

# 頂点1から最短距離を求める
# 頂点1から最も離れている頂点
for i in range(N):
    if maxn1 < dist[i]:
        maxn1 = dist[i]
        maxid1 = i

# 頂点maxid1からもっとも離れているところをさがす
maxn2 = -1
getdist(maxid1)

for i in range(N):
    maxn2 = max(maxn2, dist[i])

print(maxn2 + 1)
