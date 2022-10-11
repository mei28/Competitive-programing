from collections import deque

n, m = map(int, input().split())
INF = 10**10
G = [[-1] * (n) for _ in range(n)]
visited = [[False] * (n) for _ in range(n)]
G[0][0] = 0
visited[0][0] = True

que = deque()
que.append([0, 0])

nxy = []
for a in range(-(10**3) - 10, 10**3 + 10):
    # b=-10^3(より少し小さめ)~10^3(より少し大きめ)
    for b in range(-(10**3) - 10, 10**3 + 10):
        # a^2+b^2=Mならば
        if a**2 + b**2 == m:
            # (a,b)方向へ進める
            nxy.append([a, b])


while len(que) > 0:
    now = que.popleft()
    visited[now[0]][now[1]] = True
    for di, dj in nxy:
        ni = now[0] + di
        nj = now[1] + dj
        if 0 <= ni < n and 0 <= nj < n:
            if visited[ni][nj]:
                continue
            G[ni][nj] = G[now[0]][now[1]] + 1
            que.append([ni, nj])


for g in G:
    print(*g)
