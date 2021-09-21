import sys

sys.setrecursionlimit(5000)


def dfs(x: int, y: int) -> list:
    """dfs"""
    if x == goal[0] and y == goal[1]:
        return [(x, y)]

    maze[x][y] = "*"

    for (next_x, next_y) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if next_x < 0 or next_y < 0 or H <= next_x or W <= next_y:
            continue
        if maze[next_x][next_y] == wall or maze[next_x][next_y] == "*":
            continue

        route = dfs(next_x, next_y)
        if route:
            return [(x, y)] + route


def vec(a, b):
    return (b[0] - a[0], b[1] - a[1])


def cnt(route: list) -> int:
    cnt_ = 0
    di = vec(route[0], route[1])
    for i in range(1, len(route) - 1):
        tmp_di = vec(route[i], route[i + 1])
        if di != tmp_di:
            cnt_ += 1
        di = tmp_di
    return cnt_


if __name__ == "__main__":

    input = sys.stdin.readline
    H, W = map(int, input().split())
    rs, cs = map(int, input().split())
    rt, ct = map(int, input().split())
    start = (rs - 1, cs - 1)
    goal = (rt - 1, ct - 1)
    wall = "#"
    maze = [[i for i in input()] for i in range(H)]

    routes = dfs(start[0], start[1])
    print(cnt(routes))
