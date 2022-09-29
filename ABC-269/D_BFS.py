from collections import deque

n = int(input())
start = []
G = [[0] * 2020 for _ in range(2020)]
mer = 1005
for i in range(n):
    x, y = map(int, input().split())
    x += mer
    y += mer
    G[x][y] = 1
    start.append([x, y])


visited = [[False] * 2020 for _ in range(2020)]
dx = [-1, -1, 0, 0, 1, 1]
dy = [-1, 0, -1, 1, 0, 1]
que = deque()
ans = 0
for x, y in start:
    if not visited[x][y]:
        visited[x][y] = True
        que.append([x, y])
        ans += 1

        while 0 < len(que):
            nox, noy = que.popleft()
            for i in range(6):
                nx = nox + dx[i]
                ny = noy + dy[i]
                if G[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    que.append([nx, ny])

print(ans)
