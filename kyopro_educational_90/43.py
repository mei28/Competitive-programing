from collections import deque


class State(object):
    """Docstring for MyClass."""

    def __init__(self, x, y, direct):
        """TODO: to be defined."""
        self.x = x
        self.y = y
        self.direct = direct


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
INF = 1 << 60
if __name__ == "__main__":
    H, W = map(int, input().split())
    rs, cs = map(lambda x: int(x) - 1, input().split())
    rt, ct = map(lambda x: int(x) - 1, input().split())
    maze = [[i for i in input()] for _ in range(H)]
    dist = [[[INF for _ in range(4)] for _ in range(1010)] for _ in range(1010)]

    deq = deque()

    for i in range(4):
        dist[rs][cs][i] = 0
        deq.append((rs, cs, i))

    while len(deq) > 0:
        ur, uc, ui = deq.popleft()
        u = State(ur, uc, ui)

        for i in range(4):
            tx = u.x + dx[i]
            ty = u.y + dy[i]
            cost = 1 if u.direct != i else 0
            cost += dist[u.x][u.y][u.direct]
            if (
                0 <= tx < H
                and 0 <= ty < W
                and maze[tx][ty] == "."
                and dist[tx][ty][i] > cost
            ):
                dist[tx][ty][i] = cost
                if u.direct != i:
                    deq.append((tx, ty, i))
                else:
                    deq.appendleft((tx, ty, i))

    ans = INF

    for i in range(4):
        ans = min(ans, dist[rt][ct][i])
    print(ans)
