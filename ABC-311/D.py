from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y):
    for i in range(4):
        visited[x][y][i] = True
    q = deque([(x, y, i) for i in range(4)])

    while q:
        x, y, dir = q.popleft()
        nx, ny = x + dx[dir], y + dy[dir]
        if nx < 0 or nx >= N or ny < 0 or ny >= M or grid[nx][ny] == "#":
            for i in range(4):
                if i != dir and not visited[x][y][i]:
                    visited[x][y][i] = True
                    q.append((x, y, i))
        elif not visited[nx][ny][dir]:
            visited[nx][ny][dir] = True
            q.append((nx, ny, dir))


N, M = map(int, input().split())
grid = [list(input()) for _ in range(N)]
visited = [[[False] * 4 for _ in range(M)] for _ in range(N)]

bfs(2 - 1, 2 - 1)
reachable_ice = 0
for i in range(N):
    for j in range(M):
        reachable_ice += 1 if sum(visited[i][j]) > 0 else 0
print(reachable_ice)
