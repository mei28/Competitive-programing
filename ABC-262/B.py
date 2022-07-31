n, m = map(int, input().split())

G = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)

ans = 0
for a in range(1, n - 1):
    for b in range(a, n):
        for c in range(b, n + 1):
            if b in G[a] and c in G[b] and a in G[c]:
                ans += 1


print(ans)
