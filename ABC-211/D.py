n, m = map(int, input().split())
edge = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    edge[a].append(b)
    edge[b].append(a)

que = [0]
dist = [None] * n
cnt = [0] * n
dist[0] = 0
cnt[0] = 1

for v in que:
    for vv in edge[v]:
        if dist[vv] is None:
            dist[vv] = dist[v] + 1
            que.append(vv)
            cnt[vv] = cnt[v]
        elif dist[vv] == dist[v] + 1:
            cnt[vv] += cnt[v]
            cnt[vv] %= 1000000007

print(cnt[n - 1])
