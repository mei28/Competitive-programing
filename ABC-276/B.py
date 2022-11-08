n, m = map(int, input().split())
G = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(lambda x: int(x), map(int, input().split()))
    G[a].append(b)
    G[b].append(a)

for i in range(1, n + 1):
    print(len(G[i]), *sorted(G[i]))
