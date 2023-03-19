from collections import deque


n, m = map(int, input().split())

G = [[] for _ in range(n)]
deg = [0] * n

for _ in range(m):
    a, b, c, d = input().split()
    a = int(a) - 1
    c = int(c) - 1
    G[a].append(c)
    G[c].append(a)

    deg[a] += 1
    deg[c] += 1

x = y = 0
seen = [False] * n

for i in range(n):
    if not seen[i]:
        que = deque()
        seen[i] = True
        que.append(i)
        flg = True

        while len(que) > 0:
            q = que.popleft()
            if deg[q] != 2:
                f = False
            for v in G[q]:
                if not seen[v]:
                    que.append(v)
                    seen[v] = True
        if flg:
            x += 1
        else:
            y += 1
print(x, y)
