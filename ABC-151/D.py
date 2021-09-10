from collections import deque
from typing import List

h, w = map(int, input().split())
maze = [input() for _ in range(h)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs(maze: List[List[int]], x: int, y: int) -> int:
    """(x,y)をスタートとして一番遠いところを探す"""

    dist: List[List[int]] = [[-1] * w for _ in range(h)]
    queue = deque()

    res = -1
    # スタートの追加
    queue.append((x, y))
    dist[x][y] = 0

    while len(queue) != 0:
        q = queue.popleft()
        x, y = q[0], q[1]
        res = max(res, dist[x][y])

        for d in range(4):
            nx = dx[d] + x
            ny = dy[d] + y

            if nx < 0 or h <= nx or ny < 0 or w <= ny:
                continue
            if maze[nx][ny] == "#":
                continue
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                queue.append((nx, ny))

    return res


ans = 0

for i in range(h):
    for j in range(w):
        if maze[i][j] == "#":
            continue
        _ans = bfs(maze, i, j)
        ans = max(ans, _ans)

print(ans)
