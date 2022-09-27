from collections import deque

n, x, y = map(int, input().split())
x -= 1
y -= 1
G = [[] for _ in range(n)]

for _ in range(n - 1):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    G[u].append(v)
    G[v].append(u)

que = deque()
visited = [False] * n
prev = [-1] * n
que.append(x)
visited[x] = True
flg = False
while len(que) > 0:
    now = que.popleft()
    visited[now] = True
    for next in G[now]:
        if visited[next]:
            continue
        que.append(next)
        prev[next] = now
        if next == y:
            flg = True
            break
    if flg:
        break

ans = []
pre = y
while True:
    ans.append(y + 1)
    y = prev[y]
    if y == -1:
        break
print(*ans[::-1])
