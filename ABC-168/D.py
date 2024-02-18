from collections import deque

n, m = map(int, input().split())
G = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].append(b)
    G[b].append(a)


que = deque()
visited = [False] * (n)
ans = [-1] * (n)

que.append(0)
visited[0] = True

while len(que) > 0:
    p = que.popleft()
    for to in G[p]:
        if visited[to]:
            continue
        ans[to] = p
        visited[to] = True
        que.append(to)

print("Yes")
for i in range(1, n):
    print(ans[i] + 1)
