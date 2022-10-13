from collections import deque

n, m = map(int, input().split())

G = [[-1] * (n) for _ in range(n)]
G[0][0] = 0

que = deque()
que.append([0, 0])


def get_d(m):
    d = set()
    for i in range(n):
        for j in range(n):
            if i**2 + j**2 > m:
                break
            elif i**2 + j**2 == m:
                d |= {(i, j), (-i, j), (i, -j), (-i, -j)}
                d |= {(j, i), (-j, i), (j, -i), (-j, -i)}

    return d


d = get_d(m)
while len(que) > 0:
    x, y = que.popleft()
    cnt = G[x][y]

    for dx, dy in d:
        nx = x + dx
        ny = y + dy
        if 0 <= nx < n and 0 <= ny < n and G[nx][ny] == -1:
            G[nx][ny] = cnt + 1
            que.append([nx, ny])
for g in G:
    print(*g)
