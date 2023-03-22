from collections import deque

h, w = map(int, input().split())
S = [list(input()) for _ in range(h)]


ans = -1

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(si, sj):
    dist = [[-1] * w for _ in range(h)]
    Q = deque()
    dist[si][sj] = 0
    Q.append([si, sj])
    ret = -1
    while len(Q) > 0:
        q = Q.popleft()
        x, y = q[0], q[1]
        ret = max(ret, dist[x][y])

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or h <= nx or w <= ny:
                continue
            if S[nx][ny] == "#":
                continue
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                Q.append([nx, ny])
    return ret


for i in range(h):
    for j in range(w):
        if S[i][j] == "#":
            continue
        ans = max(ans, bfs(i, j))
print(ans)
