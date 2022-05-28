from collections import deque

h, w = map(int, input().split())
M = [list(input()) for _ in range(h)]

sx, sy = -1, -1
gx, gy = -1, -1

for i in range(h):
    for j in range(w):
        if M[i][j] == "o" and sx == -1 and sy == -1:
            sx = j
            sy = i
        elif M[i][j] == "o":
            gx = j
            gy = i

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dist = [[-1] * w for _ in range(h)]
dist[sy][sx] = 0

que = deque()
que.append([sx, sy])

while len(que) > 0:
    cx, cy = que.popleft()

    for i in range(4):
        nx = cx + dx[i]
        ny = cy + dy[i]

        if nx < 0 or ny < 0 or nx >= w or ny >= h:
            continue

        if dist[ny][nx] == -1:
            que.append([nx, ny])
            dist[ny][nx] = dist[cy][cx] + 1

print(dist[gy][gx])
