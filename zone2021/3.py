n, m = map(int, input().split())
G = [[] for _ in range(n)]

for i in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)


ans = []
max_ = -1
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            a, b, c = G[i], G[j], G[k]
            a = set(a)
            b = set(b)
            c = set(c)

            abc = a | b | c

            if len(abc) > max_:
                max_ = len(abc)
                ans = [i, j, k]
print(ans)
