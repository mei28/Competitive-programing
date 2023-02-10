from collections import deque


n, X, Y = map(int, input().split())
diff = 200
G = [[True] * (401) for _ in range(401)]
visited = [[-1] * (401) for _ in range(401)]
X += diff
Y += diff


for _ in range(n):
    x, y = map(lambda x: int(x) + diff, input().split())
    G[x][y] = False

sx, sy = diff, diff
visited[sx][sy] = 0

dx = [1, 0, -1, 1, -1, 0]
dy = [1, 1, 1, 0, 0, -1]

que = deque([[sx, sy]])

while len(que) > 0:
    x, y = que.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or 401 <= nx or 401 <= ny:
            continue

        if G[nx][ny] == False:
            continue

        if visited[nx][ny] < 0:
            que.append([nx, ny])
            visited[nx][ny] = visited[x][y] + 1

        if nx == X and ny == Y:
            print(visited[nx][ny])
            exit()

print(-1)
