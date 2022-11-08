from collections import deque

h, w = map(int, input().split())
C = [input() for _ in range(h)]

G = [[-1] * w for _ in range(h)]

sx, sy = -1, -1
for i in range(h):
    for j in range(w):
        if C[i][j] == "S":
            sx = i
            sy = j
            break

que = deque()

G[sx][sy] = 0

que.append([sx, sy, -1])
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

while len(que) > 0:
    x, y, j = que.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or h <= nx or w <= ny:
            continue
        if C[nx][ny] == "#":
            continue
        if G[nx][ny] < 0:
            if G[nx][ny] >= 2:
                print("Yes")
                [print(*g) for g in G]
                exit()
            G[nx][ny] = G[x][y] + 1
            que.append([nx, ny])
print("No")
