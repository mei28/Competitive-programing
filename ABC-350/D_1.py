from collections import deque

N, M = map(int, input().split())
g = {i: set() for i in range(1, N + 1)}

for _ in range(M):
    a, b = map(int, input().split())
    g[a].add(b)
    g[b].add(a)

flag = [False] * (N + 1)
ans = 0
for i in range(1, N + 1):
    if flag[i]:
        continue
    q = deque([i])
    flag[i] = True
    n = 0
    while q:
        gi = q.popleft()
        n += 1
        for gj in g[gi]:
            if not flag[gj]:
                flag[gj] = True
                q.append(gj)
    ans += n * (n - 1) // 2

print(ans - M)
