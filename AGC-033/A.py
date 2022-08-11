from collections import deque

h, w = map(int, input().split())

mat = [input() for _ in range(h)]

dist = [[-1] * w for _ in range(h)]

que = deque()
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(h):
    for j in range(w):
        if mat[i][j] == "#":
            dist[i][j] = 0
            que.append((i, j))

while len(que) > 0:
    cur = que.popleft()
    for dir in range(4):
        nx = cur[0] + dx[dir]
        ny = cur[1] + dy[dir]

        if nx < 0 or ny < 0 or h <= nx or w <= ny:
            continue

        if dist[nx][ny] == -1:
            dist[nx][ny] = dist[cur[0]][cur[1]] + 1
            que.append((nx, ny))

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, dist[i][j])


print(ans)
