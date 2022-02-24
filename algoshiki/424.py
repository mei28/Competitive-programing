from queue import Queue

h, w = map(int, input().split())
sx, sy, ex, ey = map(int, input().split())

mat = [list(input()) for _ in range(h)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

dist = [[-1] * w for _ in range(h)]

que = Queue()

dist[sx][sy] = 0
que.put((sx, sy))

while not que.empty():
    nx, ny = que.get()

    for xx, yy in zip(dx, dy):
        x, y = xx + nx, yy + ny

        if x < 0 or h <= x or y < 0 or w <= y or mat[x][y] == "B":
            continue
        if dist[x][y] != -1:
            continue

        dist[x][y] = dist[nx][ny] + 1
        que.put((x, y))

print(dist[ex][ey])
