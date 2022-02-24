from queue import Queue

n, m = map(int, input().split())
edge = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    edge[a].append(b)
    edge[b].append(a)


nodes = [0]

que = Queue()

dist = [-1] * n

dist[0] = 0
que.put(0)

while not que.empty() > 0:
    v = que.get()

    for n_v in edge[v]:
        if dist[n_v] != -1:
            continue

        dist[n_v] = dist[v] + 1
        que.put(n_v)

print(max(dist))
