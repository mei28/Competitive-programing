from collections import deque

h, w = map(int, input().split())
w_num: int = 0
field: list = [input() for _ in range(h)]
for i in field:
    w_num += i.count(".")
dist = [[-1] * 110 for _ in range(110)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

que: deque = deque()
dist[0][0] = 1

que.append([0, 0])

while len(que) > 0:
    cur = que.popleft()
    x = cur[0]
    y = cur[1]

    for ix, iy in zip(dx, dy):
        nx = x + ix
        ny = y + iy

        if nx < 0 or h <= nx or ny < 0 or w <= ny:
            continue
        if field[nx][ny] == "#":
            continue
        if dist[nx][ny] == -1:
            dist[nx][ny] = dist[x][y] + 1
            que.append([nx, ny])

if dist[h - 1][w - 1] == -1:
    print(-1)
else:
    print(w_num - dist[h - 1][w - 1])
