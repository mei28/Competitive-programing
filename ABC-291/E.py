from collections import deque

n, m = map(int, input().split())

G = [[] for _ in range(n)]
indegree = [0] * n

XY = []
for _ in range(m):
    x, y = map(lambda x: int(x) - 1, input().split())
    G[x].append(y)
    indegree[y] += 1
    XY.append([x, y])

ans = list(v for v in range(n) if indegree[v] == 0)

deq = deque(ans)

used = [0] * n

while deq:
    v = deq.popleft()
    for t in G[v]:
        indegree[t] -= 1
        if indegree[t] == 0:
            deq.append(t)
            ans.append(t)

print(ans)
for x, y in XY:
    if ans[x] >= ans[y]:
        print("No")
